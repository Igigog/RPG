def _hide_all(app):
    app.loadbtn.hide()  # start mode
    app.startbtn.hide()

    app.savebtn.hide()  # main mode
    app.fndbtn.hide()
    app.srbtn.hide()
    app.mapbtn.hide()
    app.invbtn.hide()

    app.escbtn.hide()   # fight mode
    app.atkbtn.hide()

    app.cngwpnbtn.hide()   # inv mode
    app.wpnbox.hide()
    app.extinvbtn.hide()
    app.armorbox.hide()
    app.cngarmorbtn.hide()

    app.extmapbtn.hide()    # map mode
    app.cnglocbtn.hide()
    app.mapbox.hide()
    app.marketbtn.hide()

    app.markettab.hide()    # market mode
    app.extmarket.hide()
    app.buybtn.hide()
    app.sellbtn.hide()
    app.marketbox.hide()


def main_mode(app):
    _hide_all(app)

    app.savebtn.show()
    app.invbtn.show()
    app.fndbtn.show()
    app.srbtn.show()
    app.mapbtn.show()


def fight_mode(app):
    _hide_all(app)

    app.escbtn.show()
    app.atkbtn.show()


def inv_mode(app):
    _hide_all(app)

    app.cngarmorbtn.show()
    app.armorbox.show()
    app.extinvbtn.show()
    app.wpnbox.show()
    app.cngwpnbtn.show()


def dead_mode(app):
    app.label.setText(app.label.text() + 'You lose! Try again next time!')
    _hide_all(app)

    app.startbtn.show()
    app.loadbtn.show()


def map_mode(app):
    _hide_all(app)

    app.mapbox.show()
    app.extmapbtn.show()
    app.cnglocbtn.show()
    app.marketbtn.show()


def market_mode(app):
    _hide_all(app)

    app.markettab.show()
    app.buybtn.show()
    app.extmarket.show()
    app.marketbox.show()
    app.sellbtn.show()
