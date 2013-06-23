import tempfile
import shutil
from sprinter import environment
import httpretty


class TestLifecycle(object):
    """
    Test the sprinter lifecycle
    """

    @httpretty.activate
    def test_full_lifecycle(self):
        """ Test the full sprinter lifecycle """
        temp_directory = tempfile.mkdtemp()
        try:
            TEST_URI = "http://testme.com/test.cfg"
            httpretty.register_uri(httpretty.GET, TEST_URI,
                                   body=open("./test_data/test_setup.cfg").read())
            env = environment.Environment(root=temp_directory)
            env.target = TEST_URI
            env.install()
            #env = environment.Environment(root=temp_directory)
            #env.source = TEST_URI
            #env.remove()
        finally:
            shutil.rmtree(temp_directory)
