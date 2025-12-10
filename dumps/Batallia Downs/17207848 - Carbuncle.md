# 17207848 - Carbuncle

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Batallia Downs (ID: 105) |
| Block Size       | 876 bytes                |
| Total Events     | 3                        |
| References Count | 33                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [901](#event-901)        | 0x0001       |    706 |             95 |
| [65535.1](#event-655351) | 0x02C3       |      7 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0064      |         100 |
|       1 | 0x00C8      |         200 |
|       2 | 0x0000      |           0 |
|       3 | 0x0013      |          19 |
|       4 | 0x0001      |           1 |
|       5 | 0x00D5      |         213 |
|       6 | 0x0023      |          35 |
|       7 | 0x0004      |           4 |
|       8 | 0x0024      |          36 |
|       9 | 0x0005      |           5 |
|      10 | 0x0006      |           6 |
|      11 | 0x0026      |          38 |
|      12 | 0x0007      |           7 |
|      13 | 0x0008      |           8 |
|      14 | 0x0028      |          40 |
|      15 | 0x0009      |           9 |
|      16 | 0x000A      |          10 |
|      17 | 0x0029      |          41 |
|      18 | 0x000B      |          11 |
|      19 | 0x000C      |          12 |
|      20 | 0x0025      |          37 |
|      21 | 0x000D      |          13 |
|      22 | 0x000E      |          14 |
|      23 | 0x0027      |          39 |
|      24 | 0x000F      |          15 |
|      25 | 0x1D0C      |        7436 |
|      26 | 0x00C9      |         201 |
|      27 | 0x002A      |          42 |
|      28 | 0x003C      |          60 |
|      29 | 0x0048      |          72 |
|      30 | 0x0032      |          50 |
|      31 | 0x1D0D      |        7437 |
|      32 | 0x1D0E      |        7438 |

## String References

- **7436**: The [orange/1/2/3/red/red/blue/blue/yellow/yellow/green/green/indigo/indigo/violet/violet] light... I can feel its power run through me.
- **7437**: Come, <Player>. Follow me...
- **7438**: Carbuncle vanished off in the direction of the La Theine Plateau.

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

### Event 901

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 706 bytes |
| Instructions | 42        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    46 01 42 43 00 43 01  02 04 10 00 80 00 30 00   F.BC.C.......0.
0010: 4E 00 F0 FF FF 7F 46 00  45 01 80 F8 FF FF 7F F8  N.....F.E.......
0020: FF FF 7F 66 64 69 31 02  80 20 00 21 00 01 BF 02  ...fdi1.. .!....
0030: 1C 01 80 38 03 80 4E 00  28 92 06 01 80 28 92 06  ...8..N.(....(..
0040: 01 6C 28 92 06 01 02 80  04 80 1C 04 80 1C 01 80  .l(.............
0050: 4E 01 F0 FF FF 7F 92 01  F8 FF FF 7F 4E 00 27 92  N...........N.'.
0060: 06 01 80 27 92 06 01 45  05 80 F8 FF FF 7F F8 FF  ...'...E........
0070: FF 7F 73 30 30 36 02 80  45 01 80 F8 FF FF 7F F8  ..s006..E.......
0080: FF FF 7F 66 64 69 31 02  80 02 04 10 02 80 80 A5  ...fdi1.........
0090: 00 62 06 80 27 92 06 01  27 92 06 01 6D 61 69 6E  .b..'...'...main
00A0: 02 80 01 F5 01 02 04 10  07 80 80 C1 00 62 08 80  .............b..
00B0: 27 92 06 01 27 92 06 01  6D 61 69 6E 02 80 01 F5  '...'...main....
00C0: 01 02 04 10 09 80 80 DD  00 62 08 80 27 92 06 01  .........b..'...
00D0: 27 92 06 01 6D 61 69 6E  02 80 01 F5 01 02 04 10  '...main........
00E0: 0A 80 80 F9 00 62 0B 80  27 92 06 01 27 92 06 01  .....b..'...'...
00F0: 6D 61 69 6E 02 80 01 F5  01 02 04 10 0C 80 80 15  main............
0100: 01 62 0B 80 27 92 06 01  27 92 06 01 6D 61 69 6E  .b..'...'...main
0110: 02 80 01 F5 01 02 04 10  0D 80 80 31 01 62 0E 80  ...........1.b..
0120: 27 92 06 01 27 92 06 01  6D 61 69 6E 02 80 01 F5  '...'...main....
0130: 01 02 04 10 0F 80 80 4D  01 62 0E 80 27 92 06 01  .......M.b..'...
0140: 27 92 06 01 6D 61 69 6E  02 80 01 F5 01 02 04 10  '...main........
0150: 10 80 80 69 01 62 11 80  27 92 06 01 27 92 06 01  ...i.b..'...'...
0160: 6D 61 69 6E 02 80 01 F5  01 02 04 10 12 80 80 85  main............
0170: 01 62 11 80 27 92 06 01  27 92 06 01 6D 61 69 6E  .b..'...'...main
0180: 02 80 01 F5 01 02 04 10  13 80 80 A1 01 62 14 80  .............b..
0190: 27 92 06 01 27 92 06 01  6D 61 69 6E 02 80 01 F5  '...'...main....
01A0: 01 02 04 10 15 80 80 BD  01 62 14 80 27 92 06 01  .........b..'...
01B0: 27 92 06 01 6D 61 69 6E  02 80 01 F5 01 02 04 10  '...main........
01C0: 16 80 80 D9 01 62 17 80  27 92 06 01 27 92 06 01  .....b..'...'...
01D0: 6D 61 69 6E 02 80 01 F5  01 02 04 10 18 80 80 F5  main............
01E0: 01 62 17 80 27 92 06 01  27 92 06 01 6D 61 69 6E  .b..'...'...main
01F0: 02 80 01 F5 01 48 19 80  23 45 1A 80 F8 FF FF 7F  .....H..#E......
0200: F8 FF FF 7F 77 68 6F 31  02 80 1C 01 80 02 05 10  ....who1........
0210: 0A 80 00 97 02 62 1B 80  27 92 06 01 27 92 06 01  .....b..'...'...
0220: 6D 61 69 6E 02 80 45 05  80 28 92 06 01 28 92 06  main..E..(...(..
0230: 01 73 30 30 36 02 80 45  1A 80 F8 FF FF 7F F8 FF  .s006..E........
0240: FF 7F 77 68 69 31 02 80  6C 28 92 06 01 02 80 04  ..whi1..l(......
0250: 80 1C 04 80 4E 00 28 92  06 01 1C 1C 80 6C 28 92  ....N.(......l(.
0260: 06 01 00 80 1D 80 1C 1E  80 48 1F 80 23 1C 1E 80  .........H..#...
0270: 6C 28 92 06 01 02 80 00  80 1C 00 80 48 20 80 23  l(..........H .#
0280: 45 1A 80 F8 FF FF 7F F8  FF FF 7F 77 68 6F 31 02  E..........who1.
0290: 80 1C 01 80 01 97 02 4E  00 F0 FF FF 7F 52 05 80  .......N.....R..
02A0: F8 FF FF 7F F8 FF FF 7F  73 30 30 36 46 00 45 1A  ........s006F.E.
02B0: 80 F8 FF FF 7F F8 FF FF  7F 77 68 69 31 02 80 20  .........whi1.. 
02C0: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0001 [0x46] CAMERA_CONTROL: Disable user control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  3: 0x0006 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  4: 0x0008 [0x02] IF !(Work_Zone[4] == 100*) GOTO 0x0030
  5: 0x0010 [0x4E] SET_ENTITY_HIDE_FLAG: Show LocalPlayer
  6: 0x0016 [0x46] CAMERA_CONTROL: Restore default settings
  7: 0x0018 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  8: 0x0029 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  9: 0x002B [0x21] END_EVENT
 10: 0x002C [0x00] END_REQSTACK()

SUBROUTINE_01F5:
 11: 0x01F5 [0x48] [System] [7436*]:
    → "The [orange/1/2/3/red/red/blue/blue/yellow/yellow/green/green/indigo/indigo/violet/violet] light... I can feel its power run through me."
 12: 0x01F8 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x01F9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 14: 0x020A [0x1C] WAIT(200* ticks)
 15: 0x020D [0x02] IF !(Work_Zone[5] == 6*) GOTO 0x0297
 16: 0x0215 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [EFFECTER (ID: 17207847/0x01069227), EFFECTER (ID: 17207847/0x01069227)], work=[42*, 0*]
 17: 0x0226 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s006" with entities [Carbuncle (ID: 17207848/0x01069228), Carbuncle (ID: 17207848/0x01069228)], work=[213*, 0*]
 18: 0x0237 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 19: 0x0248 [0x6C] FADE_ENTITY_COLOR(entity_id=Carbuncle (ID: 17207848/0x01069228), end_alpha=0*, fade_time=1*)
 20: 0x0251 [0x1C] WAIT(1* ticks)
 21: 0x0254 [0x4E] SET_ENTITY_HIDE_FLAG: Show Carbuncle (ID: 17207848/0x01069228)
 22: 0x025A [0x1C] WAIT(60* ticks)
 23: 0x025D [0x6C] FADE_ENTITY_COLOR(entity_id=Carbuncle (ID: 17207848/0x01069228), end_alpha=100*, fade_time=72*)
 24: 0x0266 [0x1C] WAIT(50* ticks)
 25: 0x0269 [0x48] [System] [7437*]:
    → "Come, <Player>. Follow me..."
 26: 0x026C [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x026D [0x1C] WAIT(50* ticks)
 28: 0x0270 [0x6C] FADE_ENTITY_COLOR(entity_id=Carbuncle (ID: 17207848/0x01069228), end_alpha=0*, fade_time=100*)
 29: 0x0279 [0x1C] WAIT(100* ticks)
 30: 0x027C [0x48] [System] [7438*]:
    → "Carbuncle vanished off in the direction of the La Theine Plateau."
 31: 0x027F [0x23] WAIT_FOR_DIALOG_INTERACTION
 32: 0x0280 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [EventEntity, EventEntity], work=[201*, 0*]
 33: 0x0291 [0x1C] WAIT(200* ticks)
 34: 0x0294 [0x01] GOTO 0x0297

SUBROUTINE_0297:
 35: 0x0297 [0x4E] SET_ENTITY_HIDE_FLAG: Show LocalPlayer
 36: 0x029D [0x52] END_LOAD_SCHEDULER: End scheduler "s006" with entities [EventEntity, EventEntity], work=213*
 37: 0x02AC [0x46] CAMERA_CONTROL: Restore default settings
 38: 0x02AE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [EventEntity, EventEntity], work=[201*, 0*]

SUBROUTINE_02BF:
 39: 0x02BF [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 40: 0x02C1 [0x21] END_EVENT
 41: 0x02C2 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x002D [0x01] GOTO 0x02BF
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x02C3  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02C0:          92 01 F8 FF FF  7F 00                       .......      
```

#### Opcodes

```
  0: 0x02C3 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x02C9 [0x00] END_REQSTACK()
```
