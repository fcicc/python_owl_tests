from owlready2 import get_ontology, onto_path, sync_reasoner

onto = get_ontology("http://www.lesfleursdunormal.fr/static/_downloads/pizza_onto.owl")
onto.load()


class NonVegetarianPizza(onto.Pizza):
    equivalent_to = [
        onto.Pizza & (onto.has_topping.some(onto.MeatTopping) | onto.has_topping.some(onto.FishTopping))
    ]


if __name__ == "__main__":
    my_pizza = onto.Pizza('my_pizza')
    my_pizza.has_topping = [ onto.CheeseTopping(), onto.TomatoTopping(), onto.MeatTopping() ]

    print('Before reasoning: %s' % my_pizza.__class__)
    sync_reasoner(debug=0)
    print('After reasoning: %s' % my_pizza.__class__)
