from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    list_set = txt_importer(path_file)

    file_info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(list_set),
        "linhas_do_arquivo": list_set,
    }

    instance.enqueue(file_info)

    print(file_info)

    return None


def remove(instance):
    try:
        removed_file = instance.dequeue()
        return print(
            f"Arquivo {removed_file['nome_do_arquivo']} removido com sucesso\n"
        )
    except IndexError:
        print("Não há elementos")


def file_metadata(instance, position):
    try:
        search = instance.search(position)
        print(search)
    except IndexError:
        sys.stderr.write("Posição inválida")
        return None

    return None
