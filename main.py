from subprocess import run


def print_hi(name):
    run("chmod 700 certGen.sh", shell=True)
    run("./certGen.sh create_device_certificate mydevice", shell=True)
    run("cd ./certs && cat new-device.cert.pem azure-iot-test-only.intermediate.cert.pem azure-iot-test-only.root.ca.cert.pem > new-device-full-chain.cert.pem ")
    print(run("ping www.baidu.com").stdout.lines)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')