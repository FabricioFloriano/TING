from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)['nome_do_arquivo'] == path_file:
            return None
        
    list_set = sorted(set(txt_importer(path_file)))

    file_info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(list_set),
        "linhas_do_arquivo": list_set,
    }

    instance.enqueue(file_info)

    print(file_info)

    return None


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""

