"""Application (b): print queue simulation using a FIFO queue."""

from linked_queue import LinkedQueue


def run_print_queue(jobs):
    """jobs: list of (job_id, pages). Prints in FIFO order, reports wait order."""
    queue = LinkedQueue()
    for job_id, pages in jobs:
        queue.enqueue((job_id, pages))
        print(f"Enqueued job {job_id} ({pages} pages)")

    print("\nPrinting in FIFO order:")
    order, pages_ahead = 1, 0
    while not queue.is_empty():
        job_id, pages = queue.dequeue()
        print(f"  #{order}: Job {job_id} - {pages} pages "
              f"(waited behind {order - 1} job(s), {pages_ahead} page(s))")
        pages_ahead += pages
        order += 1
    print(f"\nAll jobs printed. Total pages: {pages_ahead}")


if __name__ == "__main__":
    run_print_queue([("DOC-1", 5), ("DOC-2", 12), ("DOC-3", 2)])
