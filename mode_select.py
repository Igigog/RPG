def _hide_main(app):
    app.savebtn.hide()
    app.fndbtn.hide()
    app.srbtn.hide()
    app.mapbtn.hide()
    app.invbtn.hide()


def _hide_fight(app):
    app.escbtn.hide()
    app.atkbtn.hide()


def _hide_inv(app):
    app.cngwpnbtn.hide()
    app.wpnbox.hide()
    app.extinvbtn.hide()
    app.armorbox.hide()
    app.cngarmorbtn.hide()


def _hide_map(app):
    app.extmapbtn.hide()
    app.cnglocbtn.hide()
    app.mapbox.hide()


def main_mode(app):
    _hide_fight(app)
    _hide_inv(app)
    _hide_map(app)

    app.savebtn.show()
    app.invbtn.show()
    app.fndbtn.show()
    app.srbtn.show()
    app.mapbtn.show()


def fight_mode(app):
    _hide_main(app)
    _hide_inv(app)

    app.escbtn.show()
    app.atkbtn.show()


def inv_mode(app):
    _hide_main(app)

    app.cngarmorbtn.show()
    app.armorbox.show()
    app.extinvbtn.show()
    app.wpnbox.show()
    app.cngwpnbtn.show()


def dead_mode(app):
    app.label.setText(app.label.text() + 'You lose! Try again next time!')
    _hide_fight(app)

    app.startbtn.show()
    app.loadbtn.show()


def map_mode(app):
    _hide_main(app)

    app.mapbox.show()
    app.extmapbtn.show()
    app.cnglocbtn.show()

