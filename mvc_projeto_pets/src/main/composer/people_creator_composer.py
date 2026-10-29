from ....src.controllers.people_creator_controller import PeopleCreatorController
from ....src.models.postgre.repositories.people_repository import PeopleRepository
from ....src.models.postgre.settings.connection import db_connection_handler
from ....src.views.people_creator_view import PeopleCreatorView


def people_creator_composer():
    model = PeopleRepository(db_connection_handler)
    controller = PeopleCreatorController(model)
    view = PeopleCreatorView(controller)

    return view
