import os
import argparse
import sys

def generate_m3u(folder_path, repeat_count, extensions):
    # 转换为绝对路径并检查是否存在
    abs_folder = os.path.abspath(folder_path)
    if not os.path.isdir(abs_folder):
        print(f"错误: 路径 '{abs_folder}' 不是一个有效的文件夹。")
        sys.exit(1)

    # 获取视频文件并排序
    video_files = [
        os.path.join(abs_folder, f) 
        for f in os.listdir(abs_folder) 
        if f.lower().endswith(tuple(extensions))
    ]
    video_files.sort()

    if not video_files:
        print(f"在 {abs_folder} 中未找到指定的视频文件。")
        return

    # 构造 M3U 内容
    m3u_content = ["#EXTM3U"]
    for file_path in video_files:
        # 重复指定次数
        m3u_content.extend([file_path] * repeat_count)

    # 生成文件名并保存
    output_name = f"playlist_x{repeat_count}.m3u"
    output_path = os.path.join(abs_folder, output_name)

    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(m3u_content))
        print(f"成功生成播放列表: {output_path}")
        print(f"统计: 共有 {len(video_files)} 个源文件，总计 {len(m3u_content)-1} 个播放项。")
    except Exception as e:
        print(f"文件写入失败: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="将文件夹下的视频按指定次数生成 M3U 播放列表")
    
    # 必需参数：文件夹路径
    parser.add_argument("path", help="视频文件夹的路径")
    
    # 可选参数：重复次数 (默认1)
    parser.add_argument("-n", "--number", type=int, default=1, help="每个文件的播放次数 (默认: 1)")
    
    # 可选参数：自定义后缀名
    parser.add_argument("-e", "--ext", nargs='+', 
                        default=['.mp4', '.mkv', '.avi', '.mov', '.mp3', '.wav'], 
                        help="指定文件后缀名 (例如: .mp4 .ts)")

    args = parser.parse_args()

    generate_m3u(args.path, args.number, args.ext)