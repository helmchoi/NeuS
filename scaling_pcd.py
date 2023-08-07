import numpy as np
import open3d as o3d
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--case', type=str, default='')

args = parser.parse_args()
CASE_NAME = args.case

pcd_ = o3d.io.read_point_cloud("./exp/" + CASE_NAME + "/womask/points00300000.ply")
pcd_pts_ = np.asarray(pcd_.points)

cam_sphere = np.load("./data/1.wire_final_results/" + CASE_NAME + "/preprocessed/cameras_sphere.npz")
sca0 = cam_sphere['scale_mat_0']
sca29 = cam_sphere['scale_mat_29']
print("sca0:\n", sca0)
print("sca29:\n", sca29)
assert((sca0 == sca29).all())

pcd_pts_1 = np.concatenate([pcd_pts_, np.ones((len(pcd_pts_), 1))], axis=-1)
pcd_pts = pcd_pts_1 @ sca0.T

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(pcd_pts[:,0:3])
o3d.io.write_point_cloud("./exp/" + CASE_NAME + "/womask/scaledPCD.ply", pcd)
