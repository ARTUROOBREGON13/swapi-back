import graphene
from graphql_relay import from_global_id

from .models import People, Planet
from .types import PeopleType, PlanetType
from .utils import generic_model_mutation_process


class CreateOrUpdatePlanetMutation(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=False)
        name = graphene.String(required=True)
        rotation_period = graphene.String(required=False)
        orbital_period = graphene.String(required=False)
        diameter = graphene.String(required=False)
        climate = graphene.String(required=False)
        gravity = graphene.String(required=False)
        terrain = graphene.String(required=False)
        surface_water = graphene.String(required=False)
        population = graphene.String(required=False)

    planet = graphene.Field(PlanetType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        raw_id = input.get('id', None)

        data = {'model': Planet, 'data': input}
        if raw_id:
            data['id'] = from_global_id(raw_id)[1]

        planet = generic_model_mutation_process(**data)
        return CreateOrUpdatePlanetMutation(planet=planet)


class CreateOrUpdatePeopleMutation(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=False)
        height = graphene.String(required=False)
        mass = graphene.String(required=False)
        hair_color = graphene.Enum("PeopleHairEnum", People.HAIR_COLOR)
        skin_color = graphene.String(required=False)
        eye_color = graphene.Enum("PeopleEyeEnum", People.EYE_COLOR)
        birth_year = graphene.String(required=False)
        gender = graphene.Enum("PeopleHairEnum", People.GENDER)
        home_world = graphene.ID(required=True)

    people = graphene.Field(PeopleType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        raw_id = input.get('id', None)

        home_world = input.get("home_world", None)

        data = {
            "model": People,
            "data": input
        }
        if raw_id:
            data['id'] = from_global_id(raw_id)[1]

        if home_world:
            data["data"]["home_world"] = Planet.objects.get(
                id=from_global_id(home_world)[1],
            )

        people = generic_model_mutation_process(**data)
        return CreateOrUpdatePeopleMutation(people=people)
