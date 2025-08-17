# 17772686 - DoorSan dOrian Emb

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 1300 bytes                |
| Total Events     | 3                         |
| References Count | 33                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [39](#event-39)       | 0x0001       |    493 |             71 |
| [130](#event-130)     | 0x01EE       |    643 |             98 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x009C      |         156 |
|       3 | 0x01B2      |         434 |
|       4 | 0x0003      |           3 |
|       5 | 0x008F      |         143 |
|       6 | 0x003C      |          60 |
|       7 | 0x2749      |       10057 |
|       8 | 0x0096      |         150 |
|       9 | 0x001E      |          30 |
|      10 | 0x274C      |       10060 |
|      11 | 0x274F      |       10063 |
|      12 | 0x2752      |       10066 |
|      13 | 0x0022      |          34 |
|      14 | 0x00C9      |         201 |
|      15 | 0x00D2      |         210 |
|      16 | 0x2758      |       10072 |
|      17 | 0x000F      |          15 |
|      18 | 0x005A      |          90 |
|      19 | 0x0075      |         117 |
|      20 | 0x2764      |       10084 |
|      21 | 0x2767      |       10087 |
|      22 | 0x276A      |       10090 |
|      23 | 0x2770      |       10096 |
|      24 | 0x2773      |       10099 |
|      25 | 0x2774      |       10100 |
|      26 | 0x0001      |           1 |
|      27 | 0x2777      |       10103 |
|      28 | 0x0002      |           2 |
|      29 | 0x0038      |          56 |
|      30 | 0x277A      |       10106 |
|      31 | 0x277B      |       10107 |
|      32 | 0x2780      |       10112 |

## String References

- **10099**: Proceed to the archduke's palace? [Right away./Let me think about it.]

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 39

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 493 bytes |
| Instructions | 71        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 42 45 00 80 F0  FF FF 7F F0 FF FF 7F 66    .BE..........f
0010: 64 6F 31 01 80 55 00 80  F0 FF FF 7F F0 FF FF 7F  do1..U..........
0020: 66 64 6F 31 5C 00 02 80  5C 01 02 80 75 00 03 80  fdo1\...\...u...
0030: 75 01 38 04 80 46 01 29  03 F0 FF FF 7F 02 79 00  u.8..F.)......y.
0040: 02 30 0F 01 F0 FF FF 7F  79 00 F0 FF FF 7F 02 30  .0......y......0
0050: 0F 01 45 05 80 F0 FF FF  7F F0 FF FF 7F 63 6D 61  ..E..........cma
0060: 30 01 80 55 05 80 F0 FF  FF 7F F0 FF FF 7F 63 6D  0..U..........cm
0070: 61 30 4C 45 00 80 F0 FF  FF 7F F0 FF FF 7F 66 64  a0LE..........fd
0080: 69 31 01 80 55 00 80 F0  FF FF 7F F0 FF FF 7F 66  i1..U..........f
0090: 64 69 31 1C 06 80 2B 02  30 0F 01 07 80 23 27 03  di1...+.0....#'.
00A0: 02 30 0F 01 03 27 03 F0  FF FF 7F 03 1C 08 80 4D  .0...'.........M
00B0: 45 05 80 F0 FF FF 7F F0  FF FF 7F 63 6D 61 31 01  E..........cma1.
00C0: 80 55 05 80 F0 FF FF 7F  F0 FF FF 7F 63 6D 61 31  .U..........cma1
00D0: 1C 09 80 29 04 F0 FF FF  7F 33 29 04 02 30 0F 01  ...).....3)..0..
00E0: 0A 4A F0 FF FF 7F 02 30  0F 01 4A 02 30 0F 01 F0  .J.....0..J.0...
00F0: FF FF 7F 6F 76 02 30 0F  01 27 04 02 30 0F 01 04  ...ov.0..'..0...
0100: 2B 02 30 0F 01 0A 80 23  29 05 02 30 0F 01 09 27  +.0....#)..0...'
0110: 03 02 30 0F 01 07 1C 06  80 45 05 80 F0 FF FF 7F  ..0......E......
0120: F0 FF FF 7F 63 6D 61 32  01 80 55 05 80 F0 FF FF  ....cma2..U.....
0130: 7F F0 FF FF 7F 63 6D 61  32 2B 02 30 0F 01 0B 80  .....cma2+.0....
0140: 23 2B 02 30 0F 01 0C 80  23 7D 0D 80 45 0E 80 F0  #+.0....#}..E...
0150: FF FF 7F F0 FF FF 7F 71  73 74 63 01 80 1C 0F 80  .......qstc.....
0160: 29 04 02 30 0F 01 08 2B  02 30 0F 01 10 80 23 1C  )..0...+.0....#.
0170: 06 80 7B F0 FF FF 7F 27  03 F0 FF FF 7F 07 1C 11  ..{....'........
0180: 80 45 05 80 F0 FF FF 7F  F0 FF FF 7F 63 6D 61 33  .E..........cma3
0190: 01 80 55 05 80 F0 FF FF  7F F0 FF FF 7F 63 6D 61  ..U..........cma
01A0: 33 4C 1C 12 80 4D 45 00  80 F0 FF FF 7F F0 FF FF  3L...ME.........
01B0: 7F 66 64 6F 32 01 80 55  00 80 F0 FF FF 7F F0 FF  .fdo2..U........
01C0: FF 7F 66 64 6F 32 5C 00  13 80 5C 01 13 80 46 00  ..fdo2\...\...F.
01D0: 7B 02 30 0F 01 4E 01 02  30 0F 01 45 00 80 F0 FF  {.0..N..0..E....
01E0: FF 7F F0 FF FF 7F 66 64  69 32 01 80 21 00        ......fdi2..!.  
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x0015 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
  4: 0x0024 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 156*
  5: 0x0028 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 156*
  6: 0x002C [0x75] LOAD_ROOM(Load indoor room, room=434*)
  7: 0x0030 [0x75] LOAD_ROOM(No action)
  8: 0x0032 [0x38] SET_CLIENT_EVENT_MODE(mode=3*)
  9: 0x0035 [0x46] CAMERA_CONTROL: Disable user control
 10: 0x0037 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=LocalPlayer, tag_num=0x02)
 11: 0x003E [0x79] Jima (ID: 17772546/0x010F3002) looks at LocalPlayer (Basic look)
 12: 0x0048 [0x79] LocalPlayer looks at Jima (ID: 17772546/0x010F3002) (Basic look)
 13: 0x0052 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cma0" with entities [LocalPlayer, LocalPlayer], work=[143*, 0*]
 14: 0x0063 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "cma0" with entities [LocalPlayer, LocalPlayer], work=143*
 15: 0x0072 [0x4C] EventEntity->StatusEvent = 8 // Open door
 16: 0x0073 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 17: 0x0084 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 18: 0x0093 [0x1C] WAIT(60* ticks)
 19: 0x0096 [0x2B] Jima (ID: 17772546/0x010F3002) [10057*]:
    → "Ah, I'm so glad to see you."
 20: 0x009D [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x009E [0x27] REQ_SET(priority=0x03, entity_id=Jima (ID: 17772546/0x010F3002), tag_num=0x03)
 22: 0x00A5 [0x27] REQ_SET(priority=0x03, entity_id=LocalPlayer, tag_num=0x03)
 23: 0x00AC [0x1C] WAIT(150* ticks)
 24: 0x00AF [0x4D] EventEntity->StatusEvent = 9 // Close door
 25: 0x00B0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cma1" with entities [LocalPlayer, LocalPlayer], work=[143*, 0*]
 26: 0x00C1 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "cma1" with entities [LocalPlayer, LocalPlayer], work=143*
 27: 0x00D0 [0x1C] WAIT(30* ticks)
 28: 0x00D3 [0x29] REQ_SET_WAIT(priority=0x04, entity_id=LocalPlayer, tag_num=0x33)
 29: 0x00DA [0x29] REQ_SET_WAIT(priority=0x04, entity_id=Jima (ID: 17772546/0x010F3002), tag_num=0x0A)
 30: 0x00E1 [0x4A] LocalPlayer looks at Jima (ID: 17772546/0x010F3002)
 31: 0x00EA [0x4A] Jima (ID: 17772546/0x010F3002) looks at LocalPlayer
 32: 0x00F3 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 33: 0x00F4 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Jima (ID: 17772546/0x010F3002) Render.Flags0 and Render.Flags3 conditions are met
 34: 0x00F9 [0x27] REQ_SET(priority=0x04, entity_id=Jima (ID: 17772546/0x010F3002), tag_num=0x04)
 35: 0x0100 [0x2B] Jima (ID: 17772546/0x010F3002) [10060*]:
    → "Thank you so much for braving the dangers and finding me. You have my thanks. Now, enough formalities..."
 36: 0x0107 [0x23] WAIT_FOR_DIALOG_INTERACTION
 37: 0x0108 [0x29] REQ_SET_WAIT(priority=0x05, entity_id=Jima (ID: 17772546/0x010F3002), tag_num=0x09)
 38: 0x010F [0x27] REQ_SET(priority=0x03, entity_id=Jima (ID: 17772546/0x010F3002), tag_num=0x07)
 39: 0x0116 [0x1C] WAIT(60* ticks)
 40: 0x0119 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cma2" with entities [LocalPlayer, LocalPlayer], work=[143*, 0*]
 41: 0x012A [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "cma2" with entities [LocalPlayer, LocalPlayer], work=143*
 42: 0x0139 [0x2B] Jima (ID: 17772546/0x010F3002) [10063*]:
    → "I hereby assign you, <Player>, to the post of attach<Player>i of the Embassy to Jeuno."
 43: 0x0140 [0x23] WAIT_FOR_DIALOG_INTERACTION
 44: 0x0141 [0x2B] Jima (ID: 17772546/0x010F3002) [10066*]:
    → "May you apply all your powers for the sake of the motherland and her friendship with Jeuno."
 45: 0x0148 [0x23] WAIT_FOR_DIALOG_INTERACTION
 46: 0x0149 [0x7D] LOAD_START_SCHEDULER_PLAYER: Load scheduler with animation_id 32781
 47: 0x014C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 48: 0x015D [0x1C] WAIT(210* ticks)
 49: 0x0160 [0x29] REQ_SET_WAIT(priority=0x04, entity_id=Jima (ID: 17772546/0x010F3002), tag_num=0x08)
 50: 0x0167 [0x2B] Jima (ID: 17772546/0x010F3002) [10072*]:
    → "Prove yourself, and I might have need of you later. When the time comes, I hope you can help me as you did before."
 51: 0x016E [0x23] WAIT_FOR_DIALOG_INTERACTION
 52: 0x016F [0x1C] WAIT(60* ticks)
 53: 0x0172 [0x7B] LocalPlayer stops talking
 54: 0x0177 [0x27] REQ_SET(priority=0x03, entity_id=LocalPlayer, tag_num=0x07)
 55: 0x017E [0x1C] WAIT(15* ticks)
 56: 0x0181 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cma3" with entities [LocalPlayer, LocalPlayer], work=[143*, 0*]
 57: 0x0192 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "cma3" with entities [LocalPlayer, LocalPlayer], work=143*
 58: 0x01A1 [0x4C] EventEntity->StatusEvent = 8 // Open door
 59: 0x01A2 [0x1C] WAIT(90* ticks)
 60: 0x01A5 [0x4D] EventEntity->StatusEvent = 9 // Close door
 61: 0x01A6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 62: 0x01B7 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=200*
 63: 0x01C6 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 117*
 64: 0x01CA [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 117*
 65: 0x01CE [0x46] CAMERA_CONTROL: Restore default settings
 66: 0x01D0 [0x7B] Jima (ID: 17772546/0x010F3002) stops talking
 67: 0x01D5 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Jima (ID: 17772546/0x010F3002)
 68: 0x01DB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 69: 0x01EC [0x21] END_EVENT
 70: 0x01ED [0x00] END_REQSTACK()
```

### Event 130

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x01EE    |
| Data Size    | 643 bytes |
| Instructions | 98        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01E0:                                            03 00                ..
01F0: 00 02 10 20 01 42 45 00  80 F0 FF FF 7F F0 FF FF  ... .BE.........
0200: 7F 66 64 6F 31 01 80 55  00 80 F0 FF FF 7F F0 FF  .fdo1..U........
0210: FF 7F 66 64 6F 31 5C 00  02 80 5C 01 02 80 75 00  ..fdo1\...\...u.
0220: 03 80 75 01 38 04 80 46  01 29 03 F0 FF FF 7F 02  ..u.8..F.)......
0230: 79 00 02 30 0F 01 F0 FF  FF 7F 79 00 01 30 0F 01  y..0......y..0..
0240: F0 FF FF 7F 79 00 F0 FF  FF 7F 02 30 0F 01 4C 1C  ....y......0..L.
0250: 06 80 45 00 80 F0 FF FF  7F F0 FF FF 7F 66 64 69  ..E..........fdi
0260: 31 01 80 45 05 80 F0 FF  FF 7F F0 FF FF 7F 63 6D  1..E..........cm
0270: 62 30 01 80 27 03 F0 FF  FF 7F 04 55 00 80 F0 FF  b0..'......U....
0280: FF 7F F0 FF FF 7F 66 64  69 31 27 03 01 30 0F 01  ......fdi1'..0..
0290: 10 29 04 F0 FF FF 7F 33  52 05 80 F0 FF FF 7F F0  .).....3R.......
02A0: FF FF 7F 63 6D 62 30 45  05 80 F0 FF FF 7F F0 FF  ...cmb0E........
02B0: FF 7F 63 6D 62 31 01 80  55 05 80 F0 FF FF 7F F0  ..cmb1..U.......
02C0: FF FF 7F 63 6D 62 31 4D  27 03 02 30 0F 01 04 2B  ...cmb1M'..0...+
02D0: 02 30 0F 01 14 80 23 2B  02 30 0F 01 15 80 23 2B  .0....#+.0....#+
02E0: 02 30 0F 01 16 80 23 27  04 02 30 0F 01 09 29 04  .0....#'..0...).
02F0: 01 30 0F 01 17 4A 01 30  0F 01 F0 FF FF 7F 1C 06  .0...J.0........
0300: 80 27 03 01 30 0F 01 11  1C 11 80 45 05 80 F0 FF  .'..0......E....
0310: FF 7F F0 FF FF 7F 63 6D  62 32 01 80 55 05 80 F0  ......cmb2..U...
0320: FF FF 7F F0 FF FF 7F 63  6D 62 32 2B 01 30 0F 01  .......cmb2+.0..
0330: 17 80 23 29 05 01 30 0F  01 16 24 18 80 01 80 01  ..#)..0...$.....
0340: 80 25 02 00 10 01 80 00  68 03 27 03 02 30 0F 01  .%......h.'..0..
0350: 04 2B 02 30 0F 01 19 80  23 27 04 02 30 0F 01 09  .+.0....#'..0...
0360: 03 01 10 1A 80 01 8E 03  02 00 10 1A 80 00 8E 03  ................
0370: 27 03 02 30 0F 01 04 2B  02 30 0F 01 1B 80 23 27  '..0...+.0....#'
0380: 04 02 30 0F 01 09 03 01  10 1C 80 01 8E 03 79 00  ..0...........y.
0390: F0 FF FF 7F 01 30 0F 01  27 03 F0 FF FF 7F 05 03  .....0..'.......
03A0: 09 10 1D 80 02 00 00 01  80 00 BE 03 2B 01 30 0F  ............+.0.
03B0: 01 1E 80 23 29 03 01 30  0F 01 15 01 C6 03 2B 01  ...#)..0......+.
03C0: 30 0F 01 1F 80 23 79 00  F0 FF FF 7F 02 30 0F 01  0....#y......0..
03D0: 4A F0 FF FF 7F 02 30 0F  01 2B 02 30 0F 01 20 80  J.....0..+.0.. .
03E0: 23 1C 06 80 7B F0 FF FF  7F 27 03 F0 FF FF 7F 07  #...{....'......
03F0: 1C 06 80 45 05 80 F0 FF  FF 7F F0 FF FF 7F 63 6D  ...E..........cm
0400: 62 31 01 80 55 05 80 F0  FF FF 7F F0 FF FF 7F 63  b1..U..........c
0410: 6D 62 31 4C 1C 06 80 45  00 80 F0 FF FF 7F F0 FF  mb1L...E........
0420: FF 7F 66 64 6F 32 01 80  55 00 80 F0 FF FF 7F F0  ..fdo2..U.......
0430: FF FF 7F 66 64 6F 32 5C  00 13 80 5C 01 13 80 7B  ...fdo2\...\...{
0440: 02 30 0F 01 7B 01 30 0F  01 4E 01 02 30 0F 01 4E  .0..{.0..N..0..N
0450: 01 01 30 0F 01 1C 06 80  46 00 4D 1C 06 80 45 00  ..0.....F.M...E.
0460: 80 F0 FF FF 7F F0 FF FF  7F 66 64 69 31 01 80 21  .........fdi1..!
0470: 00                                                .               
```

#### Opcodes

```
  0: 0x01EE [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  1: 0x01F3 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x01F5 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  3: 0x01F6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x0207 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
  5: 0x0216 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 156*
  6: 0x021A [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 156*
  7: 0x021E [0x75] LOAD_ROOM(Load indoor room, room=434*)
  8: 0x0222 [0x75] LOAD_ROOM(No action)
  9: 0x0224 [0x38] SET_CLIENT_EVENT_MODE(mode=3*)
 10: 0x0227 [0x46] CAMERA_CONTROL: Disable user control
 11: 0x0229 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=LocalPlayer, tag_num=0x02)
 12: 0x0230 [0x79] Jima (ID: 17772546/0x010F3002) looks at LocalPlayer (Basic look)
 13: 0x023A [0x79] Nelcabrit (ID: 17772545/0x010F3001) looks at LocalPlayer (Basic look)
 14: 0x0244 [0x79] LocalPlayer looks at Jima (ID: 17772546/0x010F3002) (Basic look)
 15: 0x024E [0x4C] EventEntity->StatusEvent = 8 // Open door
 16: 0x024F [0x1C] WAIT(60* ticks)
 17: 0x0252 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x0263 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cmb0" with entities [LocalPlayer, LocalPlayer], work=[143*, 0*]
 19: 0x0274 [0x27] REQ_SET(priority=0x03, entity_id=LocalPlayer, tag_num=0x04)
 20: 0x027B [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 21: 0x028A [0x27] REQ_SET(priority=0x03, entity_id=Nelcabrit (ID: 17772545/0x010F3001), tag_num=0x10)
 22: 0x0291 [0x29] REQ_SET_WAIT(priority=0x04, entity_id=LocalPlayer, tag_num=0x33)
 23: 0x0298 [0x52] END_LOAD_SCHEDULER: End scheduler "cmb0" with entities [LocalPlayer, LocalPlayer], work=143*
 24: 0x02A7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cmb1" with entities [LocalPlayer, LocalPlayer], work=[143*, 0*]
 25: 0x02B8 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "cmb1" with entities [LocalPlayer, LocalPlayer], work=143*
 26: 0x02C7 [0x4D] EventEntity->StatusEvent = 9 // Close door
 27: 0x02C8 [0x27] REQ_SET(priority=0x03, entity_id=Jima (ID: 17772546/0x010F3002), tag_num=0x04)
 28: 0x02CF [0x2B] Jima (ID: 17772546/0x010F3002) [10084*]:
    → "Thank you for coming, <Player>."
 29: 0x02D6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 30: 0x02D7 [0x2B] Jima (ID: 17772546/0x010F3002) [10087*]:
    → "This embassy has received a request from the Archduke of Jeuno to send someone for a special mission."
 31: 0x02DE [0x23] WAIT_FOR_DIALOG_INTERACTION
 32: 0x02DF [0x2B] Jima (ID: 17772546/0x010F3002) [10090*]:
    → "Due to your exemplary service at Delkfutt's Tower, I believe you to be the foremost candidate."
 33: 0x02E6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 34: 0x02E7 [0x27] REQ_SET(priority=0x04, entity_id=Jima (ID: 17772546/0x010F3002), tag_num=0x09)
 35: 0x02EE [0x29] REQ_SET_WAIT(priority=0x04, entity_id=Nelcabrit (ID: 17772545/0x010F3001), tag_num=0x17)
 36: 0x02F5 [0x4A] Nelcabrit (ID: 17772545/0x010F3001) looks at LocalPlayer
 37: 0x02FE [0x1C] WAIT(60* ticks)
 38: 0x0301 [0x27] REQ_SET(priority=0x03, entity_id=Nelcabrit (ID: 17772545/0x010F3001), tag_num=0x11)
 39: 0x0308 [0x1C] WAIT(15* ticks)
 40: 0x030B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cmb2" with entities [LocalPlayer, LocalPlayer], work=[143*, 0*]
 41: 0x031C [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "cmb2" with entities [LocalPlayer, LocalPlayer], work=143*
 42: 0x032B [0x2B] Nelcabrit (ID: 17772545/0x010F3001) [10096*]:
    → "Succeed, and you will honor us all, <Player>. I am optimistic that you will gain the archduke's countenance."
 43: 0x0332 [0x23] WAIT_FOR_DIALOG_INTERACTION
 44: 0x0333 [0x29] REQ_SET_WAIT(priority=0x05, entity_id=Nelcabrit (ID: 17772545/0x010F3001), tag_num=0x16)
 45: 0x033A [0x24] CREATE_DIALOG(message_id=10099*, default_option=0*, option_flags=0*)
    → "Proceed to the archduke's palace? [Right away./Let me think about it.]"
 46: 0x0341 [0x25] WAIT_DIALOG_SELECT()
 47: 0x0342 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0368
 48: 0x034A [0x27] REQ_SET(priority=0x03, entity_id=Jima (ID: 17772546/0x010F3002), tag_num=0x04)
 49: 0x0351 [0x2B] Jima (ID: 17772546/0x010F3002) [10100*]:
    → "Your deeds will shine upon us all!"
 50: 0x0358 [0x23] WAIT_FOR_DIALOG_INTERACTION
 51: 0x0359 [0x27] REQ_SET(priority=0x04, entity_id=Jima (ID: 17772546/0x010F3002), tag_num=0x09)
 52: 0x0360 [0x03] Work_Zone[1] = 1*
 53: 0x0365 [0x01] GOTO 0x038E
 54: 0x0368 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x038E
 55: 0x0370 [0x27] REQ_SET(priority=0x03, entity_id=Jima (ID: 17772546/0x010F3002), tag_num=0x04)
 56: 0x0377 [0x2B] Jima (ID: 17772546/0x010F3002) [10103*]:
    → "Either way, you must present yourself to the archduke as a new member of the San d'Orian diplomatic mission. It is always darkest before dawn, as they say."
 57: 0x037E [0x23] WAIT_FOR_DIALOG_INTERACTION
 58: 0x037F [0x27] REQ_SET(priority=0x04, entity_id=Jima (ID: 17772546/0x010F3002), tag_num=0x09)
 59: 0x0386 [0x03] Work_Zone[1] = 2*
 60: 0x038B [0x01] GOTO 0x038E

SUBROUTINE_038E:
 61: 0x038E [0x79] LocalPlayer looks at Nelcabrit (ID: 17772545/0x010F3001) (Basic look)
 62: 0x0398 [0x27] REQ_SET(priority=0x03, entity_id=LocalPlayer, tag_num=0x05)
 63: 0x039F [0x03] Work_Zone[9] = 56*
 64: 0x03A4 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x03BE
 65: 0x03AC [0x2B] Nelcabrit (ID: 17772545/0x010F3001) [10106*]:
    → "This is your $3."
 66: 0x03B3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 67: 0x03B4 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Nelcabrit (ID: 17772545/0x010F3001), tag_num=0x15)
 68: 0x03BB [0x01] GOTO 0x03C6
 69: 0x03BE [0x2B] Nelcabrit (ID: 17772545/0x010F3001) [10107*]:
    → "You already have $6? Well, I guess there is no need to issue a new one."
 70: 0x03C5 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_03C6:
 71: 0x03C6 [0x79] LocalPlayer looks at Jima (ID: 17772546/0x010F3002) (Basic look)
 72: 0x03D0 [0x4A] LocalPlayer looks at Jima (ID: 17772546/0x010F3002)
 73: 0x03D9 [0x2B] Jima (ID: 17772546/0x010F3002) [10112*]:
    → "Our friendship with the Jeunoans rests upon your shoulders. Luck be with you!"
 74: 0x03E0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 75: 0x03E1 [0x1C] WAIT(60* ticks)
 76: 0x03E4 [0x7B] LocalPlayer stops talking
 77: 0x03E9 [0x27] REQ_SET(priority=0x03, entity_id=LocalPlayer, tag_num=0x07)
 78: 0x03F0 [0x1C] WAIT(60* ticks)
 79: 0x03F3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cmb1" with entities [LocalPlayer, LocalPlayer], work=[143*, 0*]
 80: 0x0404 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "cmb1" with entities [LocalPlayer, LocalPlayer], work=143*
 81: 0x0413 [0x4C] EventEntity->StatusEvent = 8 // Open door
 82: 0x0414 [0x1C] WAIT(60* ticks)
 83: 0x0417 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 84: 0x0428 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=200*
 85: 0x0437 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 117*
 86: 0x043B [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 117*
 87: 0x043F [0x7B] Jima (ID: 17772546/0x010F3002) stops talking
 88: 0x0444 [0x7B] Nelcabrit (ID: 17772545/0x010F3001) stops talking
 89: 0x0449 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Jima (ID: 17772546/0x010F3002)
 90: 0x044F [0x4E] SET_ENTITY_HIDE_FLAG: Hide Nelcabrit (ID: 17772545/0x010F3001)
 91: 0x0455 [0x1C] WAIT(60* ticks)
 92: 0x0458 [0x46] CAMERA_CONTROL: Restore default settings
 93: 0x045A [0x4D] EventEntity->StatusEvent = 9 // Close door
 94: 0x045B [0x1C] WAIT(60* ticks)
 95: 0x045E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 96: 0x046F [0x21] END_EVENT
 97: 0x0470 [0x00] END_REQSTACK()
```
