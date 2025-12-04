import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { IResponse } from '../../interfaces/response';
import { IProduto } from '../../interfaces/produto';
import { enviromont } from '../../../environments/environment';


@Injectable({ providedIn: 'root' })
export class ProdutoService {
  private httpClient = inject(HttpClient);

  selecionarProdutosGet(): Observable<IResponse<IProduto[]>> {
    return this.httpClient.get<IResponse<IProduto[]>>(
      `${enviromont.baseUrl}/produto/`,
      {
        headers: { Authorization: 'Bearer ' + localStorage.getItem('access_token') }
      }
    );
  }

  atualizarProdutoPut(id: string, nome: string, marca: string, valor: number): Observable<IResponse<IProduto>> {
    return this.httpClient.put<IResponse<IProduto>>(
      `${enviromont.baseUrl}/produto/`,
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
      `${enviromont.baseUrl}/produto/`,
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
      `${enviromont.baseUrl}/produto/${id}`,
      {
        headers: { Authorization: 'Bearer ' + localStorage.getItem('access_token') }
      }
    );
  }
}

