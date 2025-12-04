import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { IResponse } from '../../interfaces/response';
import { IProduto } from '../../interfaces/produto';


@Injectable({ providedIn: 'root' })
export class ProdutoService {
  private httpClient = inject(HttpClient);

  selecionarProdutosGet(): Observable<IResponse<IProduto[]>> {
    return this.httpClient.get<IResponse<IProduto[]>>(
      'http://127.0.0.1:8000/api/v1/produto/',
      {
        headers: { Authorization: 'Bearer ' + localStorage.getItem('access_token') }
      }
    );
  }

  atualizarProdutoPut(id: string, nome: string, marca: string, valor: number): Observable<IResponse<IProduto>> {
    return this.httpClient.put<IResponse<IProduto>>(
      "http://127.0.0.1:8000/api/v1/produto/",
      {
        id, nome, marca, valor: Number(parseFloat(valor.toString()).toFixed(2))
        
      },
      {
        headers: {
          "Authorization": 'Bearer ' + localStorage.getItem('access_token'),
          "Content-Type": 'application/json'
        }
      }
    );
  }

  cadastrarProdutoPost(nome: string, marca: string, valor: number): Observable<IResponse<IProduto>> {
    return this.httpClient.post<IResponse<IProduto>>(
      'http://127.0.0.1:8000/api/v1/produto/',
      {
        nome, marca, valor: Number(parseFloat(valor.toString()).toFixed(2))
      },
      {
        headers: {
          "Authorization": 'Bearer ' + localStorage.getItem('access_token'),
          "Content-Type": 'application/json'
        }
      }
    );
  }

  deletarProduto(id: string): Observable<IResponse<void>> {
    return this.httpClient.delete<IResponse<void>>(
      `http://127.0.0.1:8000/api/v1/produto/${id}`,
      {
        headers: { Authorization: 'Bearer ' + localStorage.getItem('access_token') }
      }
    );
  }
}

