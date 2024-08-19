package com.ejemplo;

import com.ejemplo.personajes.*;

public class Juego {

    public static void main(String[] args) {
        Mago mago = new Mago("Gandalf");
        Espadachin espadachin = new Espadachin("Aragorn", 150);
        Ladron ladron = new Ladron("Frodo");

        ladron.atacar(espadachin);
        espadachin.atacar(ladron);

        mago.atacar(espadachin);
        espadachin.atacar(mago);

        mago.atacar(ladron);
        ladron.atacar(mago);

        System.out.println("Otro personaje se suma la batalla");
        System.out.println();

        Espadachin espadachin2 = new Espadachin("Faramir");

        espadachin2.atacar(espadachin);
        espadachin.atacar(espadachin2);

        System.out.println("Otro personaje se suma la batalla");
        System.out.println();

        Ladron ladron2 = new Ladron();

        ladron2.atacar(ladron);

        ladron2.atacar(ladron2);

    }
}
