def _hide_all(app):
    for x in app.buttons_dict:
        exec('app.%s.hide()' % x)

    app.wpnbox.hide()
    app.armorbox.hide()

    app.mapbox.hide()

    app.markettab.hide()
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
