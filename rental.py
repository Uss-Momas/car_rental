#!/usr/bin/python3
"""Rental Module"""
import os


def greetings():
    print("===========================")
    print("|| Welcome to car Rental ||")
    print("===========================")


def menu():
    while True:
        os.system("clear")
        greetings()
        print("O que deseja fazer?")
        print("0 - Mostrar portfólio | 1 - Alugar um carro |", end=" ")
        print("2 - Devolver um carro")
        opt = int(input())
        if opt > -1 and opt < 3:
            break
    return opt


def chosen_option(option, cars_rented=None):
    cars = ["Chevrolet Tracker", "Chevrolet Onix", "Chevrolet Spin",
            "Hyundai HB20", "Hyundai Tucson", "Fiat Uno", "Fiat Mobi",
            "Fiat Pulse"
            ]
    prices = [120, 90, 150, 85, 120, 60, 70, 130]
    if option == 0:
        portfolio(cars_rented)
    elif option == 1:
        rent_car(cars, prices, cars_rented)
    elif option == 2:
        return_rented_car(cars, prices, cars_rented)


def portfolio(cars_rented=None):
    os.system("clear")
    cars = ["Chevrolet Tracker", "Chevrolet Onix", "Chevrolet Spin",
            "Hyundai HB20", "Hyundai Tucson", "Fiat Uno", "Fiat Mobi",
            "Fiat Pulse"
            ]
    prices = [120, 90, 150, 85, 120, 60, 70, 130]
    for i in range(len(cars)):
        if cars[i] in cars_rented:
            continue
        print("[{}] {} - R$ {} /dia".format(i, cars[i], prices[i]))


def rent_car(car_list, prices_list, cars_rented=None):
    os.system("clear")
    print("[ ALUGAR ] Dê uma olhada em nosso portfolio.")
    portfolio(cars_rented)
    print("Escolha o codigo de carro:")
    car_id = int(input())
    print("Quantos dias deseja alugar:")
    days = int(input())
    price = prices_list[car_id] * days
    print("Voce escolheu o {} por {} dias.".format(car_list[car_id], days))
    print("O preco do aluguel eh: R$ {:d}".format(price))
    print("Deseja alugar?\n0- SIM | 1-NAO.")
    opt = int(input())
    if opt == 0:
        print("Parabens voce alugou o {} por {} dias".format(car_list[car_id], days))
        cars_rented.append(car_list[car_id])


def return_rented_car(cars_available, prices, cars_rented=None):
    aux = 0
    print("Segue a lista de carros alugados. Qual voce deseja devolver?")
    for i in range(len(cars_available)):
        if cars_available[i] in cars_rented:
            print("[{}] {} - R$ {} /dia".format(aux, cars_available[i], prices[i]))
            aux += 1
    if aux == 0:
        print("Nao tem carros alugados")
        return None
    print("Escolha o codigo do carro que deseja devolver: ")
    car_id = int(input())
    print("Obrigado por devolver o carro {}.".format(cars_rented[car_id]))
    cars_rented.pop(car_id)


def main():
    cars_rented = []
    while True:
        opt = menu()
        chosen_option(opt, cars_rented)
        print("==============================")
        print("0 -  continuar | 1 - sair")
        opt = int(input())
        if opt == 1:
            break


if __name__ == "__main__":
    main()
