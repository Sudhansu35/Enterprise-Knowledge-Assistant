class DeduplicationService:

    @staticmethod
    def remove_duplicates(results):

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]

        unique_docs = []
        unique_metadata = []

        seen = set()

        for doc, metadata in zip(documents, metadatas):

            if doc not in seen:
                seen.add(doc)
                unique_docs.append(doc)
                unique_metadata.append(metadata)

        results["documents"][0] = unique_docs
        results["metadatas"][0] = unique_metadata

        return results