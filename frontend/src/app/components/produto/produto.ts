import { CommonModule } from '@angular/common';
import { ChangeDetectorRef, Component, inject } from '@angular/core';
import { FormGroup, FormControl, Validators, ReactiveFormsModule } from '@angular/forms';
import { IProduto } from '../../interfaces/produto';
import { ProdutoService } from '../../services/produto/produto';
import { Router } from '@angular/router';


@Component({
  selector: 'app-produto',
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './produto.html',
  styleUrl: './produto.css',
})
export class Produto {
  httpClient = inject(ProdutoService)
  changeDetection: ChangeDetectorRef = inject(ChangeDetectorRef)
  router: Router = inject(Router);
  produtos: IProduto[] = [];
  produtoForm = new FormGroup({
    nome: new FormControl('', Validators.required),
    marca: new FormControl('', Validators.required),
    valor: new FormControl(0.0, Validators.required),
  });
  produtoEditando: IProduto | null = null;

  ngOnInit() {
    this.httpClient.selecionarProdutosGet().subscribe(
      (response) => {
        this.produtos = response.body;
        this.changeDetection.detectChanges();
      }
    );
  }

  onSubmit() {
    if (this.produtoForm.valid) {
      if (this.produtoEditando) {
        this.httpClient.atualizarProdutoPut(
          this.produtoEditando.id,
          this.produtoForm.value.nome!,
          this.produtoForm.value.marca!,
          this.produtoForm.value.valor!
        ).subscribe(
          (response) => {
            if (response.status_code === 202) {
              alert("Produto enviado para atualizar com sucesso!");
              this.produtoEditando = null;
              this.produtoForm.reset({ valor: 0.0 });
            }
          }
        );
      } else {
        this.httpClient.cadastrarProdutoPost(
          this.produtoForm.value.nome!,
          this.produtoForm.value.marca!,
          this.produtoForm.value.valor!
        ).subscribe(
          (response) => {
            if (response.status_code === 202) {
              alert("Produto enviado para cadastro com sucesso!");
              this.produtoForm.reset({ valor: 0.0 });
            }
          }
        );
      }
    }
  }

  deletarProduto(id: string) {
    this.httpClient.deletarProduto(id).subscribe(
      (response) => {
        if (response.status_code === 202) {
          alert("Produto enviado para exclusão com sucesso!");
        }
      }
    );
  }

  editarProduto(produto: IProduto) {
    this.produtoEditando = produto;
    this.produtoForm.patchValue({
      nome: produto.nome,
      marca: produto.marca,
      valor: produto.valor,
    });
  }

  cancelarEdicao() {
    this.produtoEditando = null;
    this.produtoForm.reset({ valor: 0.0 });
  }

  logout() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    this.router.navigate(['/login']);
  }
}
