from rest_framework.response import Response
from rest_framework import pagination
from collections import OrderedDict


class CustomPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 20
    page_query_param = "page"

    def get_paginated_response(self, data):
        next = None
        previous = None

        if self.page.has_next():
            next = self.page.next_page_number()
        if self.page.has_previous():
            previous = self.page.previous_page_number()

        return Response(
            {
                "results": data,
                "meta": {
                    "pagination": OrderedDict(
                        [
                            ("page", self.page.number),
                            ("pages", self.page.paginator.num_pages),
                            ("count", self.page.paginator.count),
                        ]
                    )
                },
                "links": OrderedDict(
                    [
                        ("first", self.build_link(1)),
                        ("last", self.build_link(self.page.paginator.num_pages)),
                        ("next", self.build_link(next)),
                        ("prev", self.build_link(previous)),
                    ]
                ),
            }
        )
        # response['next'] = self.get_next_link()
        # response['previous'] = self.get_previous_link()
