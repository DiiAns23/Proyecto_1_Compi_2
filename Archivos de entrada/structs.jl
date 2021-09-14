struct Actor
    nombre:: String;
    edad:: Int64;
end;

struct Pelicula 
    nombre::String;
    posicion::Int64;
end;

struct Contrato
    actor;
    pelicula;
end;

actores = ["Elizabeth Olsen", "Adam Sandler", "Christian Bale", "Jennifer Aniston"];
peliculas = ["Avengers: Age of Ultron", "Mr. Deeds", "Batman: The Dark Knight", "Marley & Me"];

function contratar(actor, pelicula)
    return Contrato(actor,pelicula);
end;

function crearActor(nombre::String, edad::Int64)
    return Actor(nombre,edad);
end;

function crearPelicula(nombre::String, posicion::Int64) 
    return Pelicula(nombre,posicion);
end;

function imprimir(contrato)
    println("Actor: ", contrato.actor.nombre, "   Edad: ", contrato.actor.edad);
    println("Pelicula: ", contrato.pelicula.nombre, "   Genero: ", contrato.pelicula.posicion);
end;

function contratos()
    for i in 1:(1*1+2)
        contrato = Contrato(Actor("",0),Pelicula("",0));
        if(i < 4)
            actor = crearActor(actores[i], i+38);
            pelicula = crearPelicula(peliculas[i], i);
            contrato = contratar(actor, pelicula);
        end;
        imprimir(contrato);    
    end;
end;

contratos();