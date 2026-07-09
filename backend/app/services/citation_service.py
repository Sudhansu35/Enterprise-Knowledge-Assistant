class CitationService:

    @staticmethod
    def build_citations(results):

        citations = []

        for metadata in results["metadatas"][0]:

            citations.append(
                {
                    "filename": metadata.get("filename"),
                    "chunk": metadata.get("chunk")
                }
            )

        return citations