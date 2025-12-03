from app.presentation.composers.worker.produto_worker_compose import ProdutoWorkerComposer


def create_produto_worker():

    produto_worker = ProdutoWorkerComposer.compose()
    produto_worker.run()