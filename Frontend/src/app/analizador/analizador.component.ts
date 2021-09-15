import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';

import { filter,take } from 'rxjs/operators';
import{
  MonacoEditorComponent,
  MonacoEditorConstructionOptions,
  MonacoEditorLoaderService,
  MonacoStandaloneCodeEditor
} from '@materia-ui/ngx-monaco-editor'
import { AnalizadorService } from '../services/analizador.service';
import { ViewChild } from '@angular/core';

@Component({
  selector: 'app-analizador',
  templateUrl: './analizador.component.html',
  styleUrls: ['./analizador.component.css']
})
export class AnalizadorComponent implements OnInit {

  @ViewChild(MonacoEditorComponent, { static: false })
  monacoComponent: MonacoEditorComponent = new MonacoEditorComponent(this.monacoLoaderService);
  editorOptions: MonacoEditorConstructionOptions = {
    theme: 'vs-dark',
    language: 'python',
    roundedSelection: true,
    autoIndent:"full"
  };
  consoleOptions: MonacoEditorConstructionOptions = {
    theme: 'vs-dark',
    language: '',
    roundedSelection: true,
    autoIndent:"full",
    readOnly:true
  };

  code = "#Hola!, Bienvenido a mi Proyecto de Compiladores 2 \nprint(\"Hola mundo JOLC\");";
  editorTexto = new FormControl('');
  console = ""
  consola = new FormControl('');
  arbol = "";
  mostrarTabla = false;
  getErrores: Array<any> = [];

  constructor(private monacoLoaderService: MonacoEditorLoaderService, private analizarService: AnalizadorService) {
    this.monacoLoaderService.isMonacoLoaded$
      .pipe(
        filter(isLoaded => isLoaded),
        take(1)
      )
      .subscribe(() => {
        monaco.editor.defineTheme('myCustomTheme', {
          base: 'vs-dark', // can also be vs or hc-black
          inherit: true, // can also be false to completely replace the builtin rules
          rules: [
            {
              token: 'comment',
              foreground: 'ffa500',
              fontStyle: 'italic underline'
            },
            { token: 'comment.js', foreground: '008800', fontStyle: 'bold' },
            { token: 'comment.css', foreground: '0000ff' } // will inherit fontStyle from `comment` above
          ],
          colors: {}
        });
      });
  }
  editorInit(editor: MonacoStandaloneCodeEditor) {
    // monaco.editor.setTheme('vs');
    editor.setSelection({
      startLineNumber: 1,
      startColumn: 1,
      endColumn: 50,
      endLineNumber: 3
    });
  }

  ngOnInit(): void {
  }

  abrir(eve:any)
  {
    let a =eve.target.files[0]
    let text=""
    if(a){
      let reader=new FileReader()
        reader.onload=ev=>{
        const resultado=ev.target?.result
        text=String(resultado)
        console.log(resultado)
        console.log(text)
        this.code=text.toString();
        
      }
      reader.readAsText(a)
    }
  }

  guardar()
  {
    this.consola.setValue("");
    if(this.editorTexto.value)
    {
      this.escribir(this.editorTexto.value,"tyty.ty","text/plain");
    }
    else
    {
      this.consola.setValue("ERROR: No se ha ejecutado ningun cambio en el archivo...");
    }
  }
  escribir(content:string, fileName:string,contenType:string)
  {
    var a = document.createElement("a");
    var archivo = new Blob([content], {type: contenType});
    a.href = URL.createObjectURL(archivo);
    a.download = fileName;
    a.click();
  }


  ast(){
    console.log(this.arbol)
    this.consola.setValue(this.arbol);
  }
  
  limpiar()
  {
    this.consola.setValue("");
  }

  analizar(){
    this.analizarService.Analizer(this.code).subscribe((res)=>{
      this.console  = res
    })
  }

  errores(){
    // var getErrores: Array<String>
    this.mostrarTabla = true;
    this.analizarService.Errores().subscribe((res)=>{
      this.getErrores = res['valores']
      var aux: Array<any> = []
      for (var x = 0; x < this.getErrores.length; x = x+1){
        var efe = this.getErrores[x].split(',');
        var a2 = {
          'tipo': efe[0],
          'desc': efe[1],
          'fila': efe[2],
          'colum': efe[3]
        }
        aux.push(a2)
      }
      this.getErrores = aux
      console.log("Valores separados: ", this.getErrores)
    })
  }

  ocultar(){
    this.mostrarTabla = false;
  }
}
