def breadcrumbs(*items):

    results = []

    for title, url in items:

        results.append(
            {
                "title": title,
                "url": url,
            }
        )

    return results
