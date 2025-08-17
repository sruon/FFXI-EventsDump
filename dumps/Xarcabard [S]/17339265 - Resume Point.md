# 17339265 - Resume Point

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Xarcabard [S] (ID: 137) |
| Block Size       | 764 bytes               |
| Total Events     | 2                       |
| References Count | 11                      |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [45](#event-45)       | 0x0001       |    693 |             75 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x003C      |          60 |
|       2 | 0x0093      |         147 |
|       3 | 0x000F      |          15 |
|       4 | 0x0001      |           1 |
|       5 | 0x00C8      |         200 |
|       6 | 0x00C9      |         201 |
|       7 | 0x002D      |          45 |
|       8 | 0x0002      |           2 |
|       9 | 0x001E      |          30 |
|      10 | 0x00D7      |         215 |

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

### Event 45

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 693 bytes |
| Instructions | 17        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 5D 00 80 01 80 1A  88 00 46 01 38 02 80 1C   B].......F.8...
0010: 03 80 AB 11 00 80 1C 04  80 30 5C 00 00 80 5C 01  .........0\...\.
0020: 00 80 9A 21 00 45 05 80  F0 FF FF 7F F0 FF FF 7F  ...!.E..........
0030: 66 64 69 30 00 80 55 05  80 F0 FF FF 7F F0 FF FF  fdi0..U.........
0040: 7F 66 64 69 30 1B 45 05  80 F0 FF FF 7F F0 FF FF  .fdi0.E.........
0050: 7F 66 64 6F 30 00 80 55  05 80 F0 FF FF 7F F0 FF  .fdo0..U........
0060: FF 7F 66 64 6F 30 1B 45  05 80 F0 FF FF 7F F0 FF  ..fdo0.E........
0070: FF 7F 66 64 69 31 00 80  55 05 80 F0 FF FF 7F F0  ..fdi1..U.......
0080: FF FF 7F 66 64 69 31 1B  45 05 80 F0 FF FF 7F F0  ...fdi1.E.......
0090: FF FF 7F 66 64 6F 31 00  80 55 05 80 F0 FF FF 7F  ...fdo1..U......
00A0: F0 FF FF 7F 66 64 6F 31  1B 45 06 80 F0 FF FF 7F  ....fdo1.E......
00B0: F0 FF FF 7F 77 68 69 31  00 80 55 06 80 F0 FF FF  ....whi1..U.....
00C0: 7F F0 FF FF 7F 77 68 69  31 1B 45 06 80 F0 FF FF  .....whi1.E.....
00D0: 7F F0 FF FF 7F 77 68 6F  31 00 80 55 06 80 F0 FF  .....who1..U....
00E0: FF 7F F0 FF FF 7F 77 68  6F 31 1B 45 06 80 F0 FF  ......who1.E....
00F0: FF 7F F0 FF FF 7F 77 68  6F 32 00 80 55 06 80 F0  ......who2..U...
0100: FF FF 7F F0 FF FF 7F 77  68 6F 32 1B 45 06 80 F0  .......who2.E...
0110: FF FF 7F F0 FF FF 7F 77  68 6F 33 00 80 55 06 80  .......who3..U..
0120: F0 FF FF 7F F0 FF FF 7F  77 68 6F 33 1B 62 04 80  ........who3.b..
0130: F0 FF FF 7F F0 FF FF 7F  6D 61 69 6E 00 80 1C 07  ........main....
0140: 80 45 05 80 F0 FF FF 7F  F0 FF FF 7F 66 64 6F 31  .E..........fdo1
0150: 00 80 55 05 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..U..........fdo
0160: 31 1B 45 05 80 F0 FF FF  7F F0 FF FF 7F 66 64 69  1.E..........fdi
0170: 31 00 80 62 08 80 F0 FF  FF 7F F0 FF FF 7F 6D 61  1..b..........ma
0180: 69 6E 00 80 1C 09 80 55  05 80 F0 FF FF 7F F0 FF  in.....U........
0190: FF 7F 66 64 69 31 1B 45  05 80 F0 FF FF 7F F0 FF  ..fdi1.E........
01A0: FF 7F 62 6C 6F 6E 00 80  45 06 80 F0 FF FF 7F F0  ..blon..E.......
01B0: FF FF 7F 62 6C 6F 6E 00  80 1B 45 06 80 F0 FF FF  ...blon...E.....
01C0: 7F F0 FF FF 7F 77 68 69  30 00 80 55 06 80 F0 FF  .....whi0..U....
01D0: FF 7F F0 FF FF 7F 77 68  69 30 1B 45 06 80 F0 FF  ......whi0.E....
01E0: FF 7F F0 FF FF 7F 77 68  6F 30 00 80 55 06 80 F0  ......who0..U...
01F0: FF FF 7F F0 FF FF 7F 77  68 6F 30 1B 45 0A 80 F0  .......who0.E...
0200: FF FF 7F F0 FF FF 7F 65  66 6F 6E 00 80 55 0A 80  .......efon..U..
0210: F0 FF FF 7F F0 FF FF 7F  65 66 6F 6E 1B 45 05 80  ........efon.E..
0220: F0 FF FF 7F F0 FF FF 7F  66 64 69 73 00 80 1B 45  ........fdis...E
0230: 05 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 73 00 80  ..........fdos..
0240: 55 05 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 73 1B  U..........fdos.
0250: 45 05 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 66 00  E..........fdif.
0260: 80 1B 45 05 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..E..........fdo
0270: 66 00 80 55 05 80 F0 FF  FF 7F F0 FF FF 7F 66 64  f..U..........fd
0280: 6F 66 1B 45 05 80 F0 FF  FF 7F F0 FF FF 7F 66 64  of.E..........fd
0290: 69 70 00 80 1B 45 05 80  F0 FF FF 7F F0 FF FF 7F  ip...E..........
02A0: 66 64 6F 70 00 80 55 05  80 F0 FF FF 7F F0 FF FF  fdop..U.........
02B0: 7F 66 64 6F 70 1B                                 .fdop.          
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x5D] SET_MUSIC_VOLUME(volume=0*, fade_time=60*)
  2: 0x0007 [0x1A] CALL_SUBROUTINE(address=0x0088)
  3: 0x000A [0x46] CAMERA_CONTROL: Disable user control
  4: 0x000C [0x38] SET_CLIENT_EVENT_MODE(mode=147*)
  5: 0x000F [0x1C] WAIT(15* ticks)
  6: 0x0012 [0xAB] EventEntity->DespawnValue = 0* // Set despawn value
  7: 0x0016 [0x1C] WAIT(1* ticks)
  8: 0x0019 [0x30] SET_UCOFF_CONTINUE_ZERO()
  9: 0x001A [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 0*
 10: 0x001E [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 0*
 11: 0x0022 [0x9A] WAIT_MUSIC_SERVER()
 12: 0x0023 [0x21] END_EVENT
 13: 0x0024 [0x00] END_REQSTACK()

SUBROUTINE_0088:
 14: 0x0088 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 15: 0x0099 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 16: 0x00A8 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0025 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0036 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0045 [0x1B] RETURN
     0x0046 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0057 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0066 [0x1B] RETURN
     0x0067 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0078 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0087 [0x1B] RETURN
# Dead code (unreachable instructions):
     0x00A9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x00BA [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=201*
     0x00C9 [0x1B] RETURN
     0x00CA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x00DB [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=201*
     0x00EA [0x1B] RETURN
     0x00EB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who2" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x00FC [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who2" with entities [LocalPlayer, LocalPlayer], work=201*
     0x010B [0x1B] RETURN
     0x010C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who3" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x011D [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who3" with entities [LocalPlayer, LocalPlayer], work=201*
     0x012C [0x1B] RETURN
     0x012D [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
     0x013E [0x1C] WAIT(45* ticks)
     0x0141 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0152 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0161 [0x1B] RETURN
     0x0162 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0173 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[2*, 0*]
     0x0184 [0x1C] WAIT(30* ticks)
     0x0187 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0196 [0x1B] RETURN
     0x0197 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x01A8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x01B9 [0x1B] RETURN
     0x01BA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi0" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x01CB [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "whi0" with entities [LocalPlayer, LocalPlayer], work=201*
     0x01DA [0x1B] RETURN
     0x01DB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who0" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x01EC [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who0" with entities [LocalPlayer, LocalPlayer], work=201*
     0x01FB [0x1B] RETURN
     0x01FC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "efon" with entities [LocalPlayer, LocalPlayer], work=[215*, 0*]
     0x020D [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "efon" with entities [LocalPlayer, LocalPlayer], work=215*
     0x021C [0x1B] RETURN
     0x021D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdis" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x022E [0x1B] RETURN
     0x022F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdos" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0240 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdos" with entities [LocalPlayer, LocalPlayer], work=200*
     0x024F [0x1B] RETURN
     0x0250 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdif" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0261 [0x1B] RETURN
     0x0262 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0273 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdof" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0282 [0x1B] RETURN
     0x0283 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdip" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0294 [0x1B] RETURN
     0x0295 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdop" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x02A6 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdop" with entities [LocalPlayer, LocalPlayer], work=200*
     0x02B5 [0x1B] RETURN
```
