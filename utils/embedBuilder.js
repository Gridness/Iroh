const Discord = require('discord.js');

function buildEmbed(client, message, color, title, description) {
    let embed = new Discord.MessageEmbed()
    .setColor(color)
    .setFooter(client.user.username, client.user.displayAvatarURL());
    if(title) embed.setTitle(title);
    if(description) embed.setDescription(description);
    message.channel.send(embed);
}

module.exports = {
    buildEmbed
}