import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {HttpClientModule} from '@angular/common/http'

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AnalizadorComponent } from './analizador/analizador.component';
import { MonacoEditorModule,MONACO_PATH } from '@materia-ui/ngx-monaco-editor';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations'
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    AnalizadorComponent,

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MonacoEditorModule,
    ReactiveFormsModule,
    FormsModule,
    BrowserAnimationsModule,
    HttpClientModule
  ],
  providers: [
    {
      provide: MONACO_PATH,
      useValue: 'https://unpkg.com/monaco-editor@0.19.3/min/vs'
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
