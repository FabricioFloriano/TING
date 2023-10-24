from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    result_search_word = []

    for index in range(len(instance)):
        instance_object = instance.search(index)
        lines = instance_object.get("linhas_do_arquivo")
        file_name = instance_object.get("nome_do_arquivo")

        if lines and file_name:
            ocorrencias = [
                {"linha": line_index}
                for line_index, line in enumerate(lines, 1)
                if word.lower() in line.lower()
            ]

            if ocorrencias:
                result_search_word.append(
                    {
                        "palavra": word,
                        "arquivo": file_name,
                        "ocorrencias": ocorrencias,
                    }
                )

    return result_search_word


def find_word(word, file_data):
    occurrences = []
    for line_num, line_strg in enumerate(file_data["linhas_do_arquivo"]):
        if word.lower() in line_strg.lower():
            occurrences.append({"linha": line_num + 1, "conteudo": line_strg})
    return occurrences


def search_by_word(word, file_queue):
    result = []

    for index in range(len(file_queue)):
        file_data = file_queue.search(index)
        occurrences = find_word(word, file_data)
        if occurrences:
            result.append(
                {
                    "palavra": word,
                    "arquivo": file_data["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )

    return result
