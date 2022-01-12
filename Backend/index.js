//Created by 6Ex#6666, removing these credits will result in a class action lawsuit against you / your corporation, under the DMCA Act.
//IGNORE MESSY CODE, I FUCKING HATE NODE JS
function makeid(length) {
    var result = '';
    var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for (var i = 0; i < length; i++) {
        result += characters.charAt(Math.floor(Math.random() *
            charactersLength));
    }
    return result;
}
var express = require('express'),
    app = express(),
    port = process.env.PORT || 3000;

app.listen(port);

console.log('todo list RESTful API server started on: ' + port);
const noblox = require('noblox.js')
async function startApp() {
    // You MUST call setCookie() before using any authenticated methods [marked by 🔐]
    // Replace the parameter in setCookie() with your .ROBLOSECURITY cookie.
    const currentUser = await noblox.setCookie('COOKIEHERE')
}
startApp();

function devDevPro(RobuxPrice, callback) {
    noblox.addDeveloperProduct(
        UNIVERSEIDHERE,
        makeid(35),
        RobuxPrice,
        "DHC"
    ).then(function(Product) {
        return callback(Product.productId);
    }).catch(function(err) {
        console.log(err)
    })
}
app.get('/create', function(req, res) {
    RobuxPrice = req.query.price
    devDevPro(RobuxPrice, function(start) {
        res.send(`${start}`)
    })
});
app.get('/', function(req, res) {
    res.send("welcome to hell bbg")
});
