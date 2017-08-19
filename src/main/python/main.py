import sys
import logging
import glfw
import vulkan as vk


logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


class Demo:
    window = None
    instance = None

    def run(self):
        logger.debug('Starting...')

        self.init_window()
        self.init_vulkan()
        self.main_loop()
        self.cleanup()

    def init_window(self):
        logger.debug('Init window')
        if not glfw.init():
            return 1

        glfw.window_hint(glfw.CLIENT_API, glfw.NO_API)
        glfw.window_hint(glfw.RESIZABLE, False)

        self.window = glfw.create_window(800, 600, "Pyrengine", None, None)

    def init_vulkan(self):
        logger.debug('Init vulkan')
        self.create_instance()
        return

    def main_loop(self):
        logger.debug('Init main loop')
        while not glfw.window_should_close(self.window):
            glfw.poll_events()

    def cleanup(self):
        logger.debug('Cleanup')
        vk.vkDestroyInstance(self.instance, None)
        glfw.destroy_window(self.window)
        glfw.terminate()

    def create_instance(self):
        application_info = vk.VkApplicationInfo(
            sType = vk.VK_STRUCTURE_TYPE_APPLICATION_INFO,
            pApplicationName = "Pyrengine Test",
            applicationVersion = vk.VK_MAKE_VERSION(1,0,0),
            pEngineName = "Pyrengine",
            engineVersion = vk.VK_MAKE_VERSION(1, 0, 0),
            apiVersion = vk.VK_API_VERSION
        )

        extensions = glfw.get_required_instance_extensions()

        instance_create_info = vk.VkInstanceCreateInfo(
            sType = vk.VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO,
            pApplicationInfo = application_info,
            enabledExtensionCount= len(extensions),
            ppEnabledExtensionNames=extensions
        )

        self.instance = vk.vkCreateInstance(instance_create_info, None)

if __name__ == "__main__":
    demo = Demo()

    try:
        demo.run()
    except:
        e = sys.exec_info()[0]
        print('Error occurred:', e)