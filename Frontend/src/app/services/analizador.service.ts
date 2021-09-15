import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class AnalizadorService {

  constructor(private http:HttpClient) { }

  headers: HttpHeaders = new HttpHeaders({
    "Content-Type": "application/json"
  });

  Analizer(codigo:String){
    const url = 'https://calm-dusk-76175.herokuapp.com/prueba'
    // const url = 'http://localhost:5200/prueba'
    return this.http.post<any>(
      url,
      {
        "codigo": codigo,
      }
    ).pipe(map(data=>data));
  }

  Errores(){
    const url = 'http://localhost:5200/errores'
    return this.http.get<any>(url)
  }
}
