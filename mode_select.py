def main_mode(app):
    app.escbtn.hide()  # hide fight mode
    app.atkbtn.hide()

    app.cngwpnbtn.hide()  # hide inv mode
    app.wpnbox.hide()
    app.extinvbtn.hide()

    app.savebtn.show()
    app.fndbtn.show()
    app.srbtn.show()


def fight_mode(app):
    app.savebtn.hide()  # hide main mode
    app.fndbtn.hide()
    app.srbtn.hide()

    app.cngwpnbtn.hide()  # hide inv mode
    app.wpnbox.hide()
    app.extinvbtn.hide()

    app.escbtn.show()
    app.atkbtn.show()


def inv_mode(app):
    app.savebtn.hide()  # hide main mode
    app.fndbtn.hide()
    app.srbtn.hide()

    app.escbtn.hide()  # hide fight mode
    app.atkbtn.hide()

    app.invbtn.hide()

    app.extinvbtn.show()
    app.wpnbox.show()
    app.cngwpnbtn.show()

def dead_mode(app):
    app.label.setText(app.label.text() + 'You lose! Try again next time!')

    app.escbtn.hide()  #hide fight mode + inv
    app.atkbtn.hide()
    app.invbtn.hide()

    app.startbtn.show()
    app.loadbtn.show()