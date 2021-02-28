//работает с божьей помощью
require('dotenv').config();

const { Client } = require('discord.js');
const client = new Client();

const DisTube = require('distube');
const { buildEmbed } = require('./utils/embedBuilder');
const { playPhrases, queuePhrases, playlistPhrases, errorPhrases } = require('./utils/phrases');
const distube = new DisTube(client, {searchSongs: true, 
    emitNewSongOnly: true, 
    highWaterMark: 1<<25});

require('./utils/loadEvents')(client)

client.on("message", async message => {
    const PREFIX = process.env.PREFIX;
    if(message.author.bot) return;

    if(!message.content.startsWith(PREFIX)) return;

    const args = message.content.slice(PREFIX.length).trim().split(/ +/g);
    const command = args.shift();

    if(command === 'play' || command === 'p') {
        buildEmbed(client, message, "ORANGE", "Вот, что мне удалось найти:", args.join(" "));
        return distube.play(message, args.join(" "));
    }

    if(command === 'pause') {
        buildEmbed(client, message, "ORANGE", "Подождем!", "");
        return distube.pause(message);
    }

    if(command === 'stop') {
        buildEmbed(client, message, "ORANGE", "Остановочка!", "");
        return distube.stop(message);
    }

    if(command === 'resume') {
        buildEmbed(client, message, "ORANGE", "Продолжаем!", "");
        return distube.resume(message);
    }

    if(command === 'skip') {
        buildEmbed(client, message, "ORANGE", "Пропускаем!", "");
        if(distube.getQueue.length < 2) {
            return;
        }
        return distube.skip(message);
    }

    if(command === 'queue' || command === 'q'){
        let queue = distube.getQueue(message);
        let curqueue = queue.songs.map((song, id) =>
        `**${id  + 1}**. ${song.name}`).join("\n");
        return buildEmbed(client, message, "ORANGE", "Под что мы будем плясать", curqueue);
    }

    if (command === "loop" || command === "repeat"){
        if(0 <= Number(args[0]) && Number(args[0]) <= 2){
            distube.setRepeatMode(message,parseInt(args[0]))
            buildEmbed(client, message, "ORANGE", "На повтор!", `${args[0].replace("0", "OFF").replace("1", "").replace("2", "")}`)
        }
        else{
            buildEmbed(client, message, "RED", errorPhrases[Math.floor(Math.random() * errorPhrases.length)], `Дай знать, что нужно сделать!   |   *0: отсанавливаемся, 1: повторяем песню, 2: повторяем очередь*`)
        }
    }

    if ( command === "jump"){
        let queue = distube.getQueue(message);
        if(0 <= Number(args[0]) && Number(args[0]) <= queue.songs.length){
            buildEmbed(client, message, "RED", errorPhrases[Math.floor(Math.random() * errorPhrases.length)], `Jumped ${parseInt(args[0])} songs!`)
            return distube.jump(message, parseInt(args[0]))
            .catch(err => message.channel.send("А что это за песня? У нас их вроде меньше!"));
        }
        else{
            buildEmbed(client, message, "RED", errorPhrases[Math.floor(Math.random() * errorPhrases.length)], `У нас всего **${DisTube.getQueue(message).length}** песен!`)
        }

    
    }
})

const status = (queue) => `Громкость: \`${queue.volume}\` | Фильтр: \`${queue.filter || "Выключен"}\` | Цикл: \`${queue.repeatMode ? queue.repeatMode === 2 ? "Вся очередь" : "Эта песня" : "Off"}\` | Автоигра: \`${queue.autoplay ? "Да" : "Нет"}\``

distube
     .on("playSong", (message, queue, song) => {
        buildEmbed(client, message, "ORANGE", playPhrases[Math.floor(Math.random() * playPhrases.length)], ` \`${song.name}\`\n\nЗаказал ${song.user}\n${status(queue)}`)
     })
     .on("addSong", (message, queue, song) => {
        buildEmbed(client, message, "ORANGE", queuePhrases[Math.floor(Math.random() * queuePhrases.length)], ` \`${song.name}\`\n\nЗаказал ${song.user}`)
     })
     .on("playList", (message, queue, playlist, song) => {
        buildEmbed(client, message, "ORANGE", playlistPhrases[Math.floor(Math.random() * playlistPhrases.length)], ` \`${playlist.title}\`  -  \`${playlist.total_items} песен всего\` \n\nЗаказал ${song.user}`)
     })
     .on("addList", (message, queue, song) => {
        buildEmbed(client, message, "ORANGE", playlistPhrases[Math.floor(Math.random() * playlistPhrases.length)], ` \`${playlist.title}\`  -  \`${playlist.total_items} песен всего\` \n\nЗаказал ${song.user}`)
     })
     .on("searchResult", (message, result) => {
        let i = 0;
        buildEmbed(client, message, "ORANGE", "", `**Вот, что мне удалось найти. Выбирай любую!**\n${result.map(song => `**${++i}**. ${song.name} - \`${song.formattedDuration}\``).join("\n")}\n*Скажи что-нибудь, кроме номера песни, если хочешь отменить заказ в течение минуты*`)
    })
     // DisTubeOptions.searchSongs = true
     .on("searchCancel", (message) =>  buildEmbed(client, message, "RED", `Заказа не будет`, "")
     )
     .on("error", (message, err) => buildEmbed(client, message, "RED", errorPhrases[Math.floor(Math.random() * errorPhrases.length)], err)
     )

client.login(process.env.TOKEN);