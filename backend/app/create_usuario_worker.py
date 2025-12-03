from app.presentation.composers.worker.usuario_worker_compose import UsuarioWorkerComposer


def create_usuario_worker():

    usuario_worker = UsuarioWorkerComposer.compose()
    usuario_worker.run()
