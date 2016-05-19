#!/usr/bin/env python

import os.path as osp

from jsk_data import download_data


def main():
    PKG = 'jsk_perception'

    download_data(
        pkg_name=PKG,
        path='trained_data/drill_svm.xml',
        url='https://drive.google.com/uc?id=0B5hRAGKTOm_KWW11R0FTX0xjTDg',
        md5='762d0da4bcbf50e0e92939372988901a',
    )

    download_data(
        pkg_name=PKG,
        path='trained_data/apc2015_sample_bof.pkl.gz',
        url='https://drive.google.com/uc?id=0B9P1L--7Wd2vemVRaDBOWDVpb28',
        md5='97eb737f71a33bfc23ec573f1d351bd8',
    )
    download_data(
        pkg_name=PKG,
        path='trained_data/apc2015_sample_clf.pkl.gz',
        url='https://drive.google.com/uc?id=0B9P1L--7Wd2veFY5ZFNqbzAzNmc',
        md5='25e396358e9d7bfd1bd08334953fc287',
    )

    files = [
        ('ObjNessB2W8HSV.idx.yml.gz', 'e066c100d60246a3911d4559182d9d2a'),
        ('ObjNessB2W8HSV.wS1.yml.gz', '728507d99521d7dba9b0eb114ccbb830'),
        ('ObjNessB2W8HSV.wS2.yml.gz', '790e27251267d86168a12f2bd2d96f8d'),
        ('ObjNessB2W8I.idx.yml.gz', '9425dd4d31521fced82aeb6fc56ce4d5'),
        ('ObjNessB2W8I.wS1.yml.gz', 'a04d4b4504887fc16800b8b42bac9e70'),
        ('ObjNessB2W8I.wS2.yml.gz', 'f2e2f5726e352bfa16224066e2bdc7ad'),
        ('ObjNessB2W8MAXBGR.idx.yml.gz', 'ef2fbd5da0ffb5fe4332685b8529dc5c'),
        ('ObjNessB2W8MAXBGR.wS1.yml.gz', 'cbe8147fca9a5885b7bb25d38fa5f4d1'),
        ('ObjNessB2W8MAXBGR.wS2.yml.gz', '02b76364df35cef862da041585b537de'),
    ]
    dirname = 'https://github.com/Itseez/opencv_contrib/raw/3.1.0/modules/saliency/samples/ObjectnessTrainedModel'  # NOQA
    for fname, md5 in files:
        download_data(
            pkg_name=PKG,
            path=osp.join('trained_data/ObjectnessTrainedModel/', fname),
            url=osp.join(dirname, fname),
            md5=md5,
        )


if __name__ == '__main__':
    main()
