import { HttpClient } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AnalizadorComponent } from './analizador/analizador.component';
import { HomeComponent } from './home/home.component';

const routes: Routes = [
  {
    path: 'analizar',
    component: AnalizadorComponent
  },
  {
    path: 'home',
    component: HomeComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { 
  constructor(private http: HttpClient){}
  uploadFile(formData:any){
    let url = ''
  }
}
