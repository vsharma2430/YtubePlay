from base.linker import download_by_search
from base.time_calc import calculate_time_console
from concurrent import futures

def thread_helper(args):
    download_by_search(args[0],args[1])

@calculate_time_console
def generate_download_threads(num, values,output_path):
    args = ((value, output_path) for value in values)
    with futures.ThreadPoolExecutor(num) as tex:
        for _ in tex.map(thread_helper,args):
            pass