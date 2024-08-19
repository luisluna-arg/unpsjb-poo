package com.ejemplo.personajes;

public class Ladron {

    private String nombre;
    private int vida;

    private static final int DANO_ESPADACHIN = 5;
    private static final int DANO_LADRON = 5;
    private static final int DANO_MAGO = 10;

    public Ladron() {
        this("Ladron Generico 44", 80);
    }

    public Ladron(String nombre, int vida) {
        this.nombre = nombre;
        this.vida = vida;
    }

    public Ladron(String nombre) {
        this(nombre, 100);
    }

    public String getNombre() {
        return nombre;
    }

    public int getVida() {
        return vida;
    }

    public void recibirDano(int dano) {
        vida -= dano;
        if (vida < 0)
            vida = 0;
    }

    public void atacar(Mago objetivo) {
        System.out.println(getNombre() + " ataca a " + objetivo.getNombre() + "!");
        objetivo.recibirDano(DANO_MAGO);
        System.out.println(objetivo.getNombre() + " tiene " + objetivo.getVida() + " puntos de vida restantes.");
        System.out.println();
    }

    public void atacar(Ladron objetivo) {
        System.out.println(getNombre() + " ataca a " + objetivo.getNombre() + "!");
        objetivo.recibirDano(DANO_LADRON);
        System.out.println(objetivo.getNombre() + " tiene " + objetivo.getVida() + " puntos de vida restantes.");
        System.out.println();
    }

    public void atacar(Espadachin objetivo) {
        System.out.println(getNombre() + " ataca a " + objetivo.getNombre() + "!");
        objetivo.recibirDano(DANO_ESPADACHIN);
        System.out.println(objetivo.getNombre() + " tiene " + objetivo.getVida() + " puntos de vida restantes.");
        System.out.println();
    }
}
