module.exports = client => {
    console.log(`${client.user.tag} is online`);
    client.user.setActivity("Музыкальная ночь!", {type: "LISTENING"})
}