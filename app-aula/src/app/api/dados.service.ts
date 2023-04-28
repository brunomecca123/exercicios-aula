import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DadosService {

  private host = 'https://jsonplaceholder.typicode.com/posts/';

  constructor(private http: HttpClient) { }

public getAllDados(){
  return new Promise((ret) => {

    this.http.get(this.host).subscribe(dados => {

      ret(dados);
    })
  })
}

}
