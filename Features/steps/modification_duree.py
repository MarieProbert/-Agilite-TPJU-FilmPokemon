from behave import given, when, then
from film import Film 

@given('un film')
def step_impl(context):
    context.mon_film = Film()
    context.mon_film.set_duree(0)

@when('je modifie la durée en {duree}')
def step_impl(context, duree):
    duree_int = int(duree)
    context.mon_film.set_duree(duree_int)

@then('la durée du film est {duree}')
def step_impl(context, duree):
    attendu = int(duree)
    reel = context.mon_film.get_duree()
    assert reel == attendu, f"ERREUR : attendu : {attendu}, obtenu : {reel}"