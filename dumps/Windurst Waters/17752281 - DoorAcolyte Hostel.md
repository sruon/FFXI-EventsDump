# 17752281 - DoorAcolyte Hostel

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 312 bytes                 |
| Total Events     | 2                         |
| References Count | 12                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [810](#event-810)     | 0x0001       |    239 |             41 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x272B      |       10027 |
|       1 | 0x00C8      |         200 |
|       2 | 0x0000      |           0 |
|       3 | 0x003C      |          60 |
|       4 | 0x0003      |           3 |
|       5 | 0x00D3      |         211 |
|       6 | 0x272C      |       10028 |
|       7 | 0x0096      |         150 |
|       8 | 0x272D      |       10029 |
|       9 | 0x272E      |       10030 |
|      10 | 0x0064      |         100 |
|      11 | 0x272A      |       10026 |

## String References

- **10026**: THAT IS INCORRECT! NO PARTING GIFTS FOR YOU!
- **10027**: YOU ARE RIGHT!

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

### Event 810

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 239 bytes |
| Instructions | 4         |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 20 00 21 00 42 46  01 48 00 80 23 45 01 80   B .!.BF.H..#E..
0010: F8 FF FF 7F F8 FF FF 7F  66 64 6F 31 02 80 1C 03  ........fdo1....
0020: 80 38 04 80 29 0B F0 FF  FF 7F 4E 4E 00 DF E0 0E  .8..).....NN....
0030: 01 80 DF E0 0E 01 4A F0  FF FF 7F DF E0 0E 01 6F  ......J........o
0040: 76 F0 FF FF 7F 45 05 80  F0 FF FF 7F F0 FF FF 7F  v....E..........
0050: 73 30 39 33 02 80 45 01  80 F8 FF FF 7F F8 FF FF  s093..E.........
0060: 7F 66 64 69 31 02 80 2B  DF E0 0E 01 06 80 23 45  .fdi1..+......#E
0070: 01 80 F8 FF FF 7F F8 FF  FF 7F 66 64 6F 31 02 80  ..........fdo1..
0080: 1C 07 80 2B DF E0 0E 01  08 80 23 1C 07 80 55 05  ...+......#...U.
0090: 80 F0 FF FF 7F F0 FF FF  7F 73 30 38 38 45 01 80  .........s088E..
00A0: F8 FF FF 7F F8 FF FF 7F  66 64 69 31 02 80 1C 03  ........fdi1....
00B0: 80 2B DF E0 0E 01 09 80  23 45 01 80 F8 FF FF 7F  .+......#E......
00C0: F8 FF FF 7F 66 64 6F 31  02 80 1C 03 80 03 01 10  ....fdo1........
00D0: 0A 80 46 00 45 01 80 F8  FF FF 7F F8 FF FF 7F 66  ..F.E..........f
00E0: 64 69 31 02 80 1B 03 01  10 02 80 48 0B 80 23 1B  di1........H..#.
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  2: 0x0004 [0x21] END_EVENT
  3: 0x0005 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0006 [0x42] SET_CLI_EVENT_CANCEL_DATA()
     0x0007 [0x46] CAMERA_CONTROL: Disable user control
     0x0009 [0x48] [System] [10027*]:
    → "YOU ARE RIGHT!"
     0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x000D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
     0x001E [0x1C] WAIT(60* ticks)
     0x0021 [0x38] SET_CLIENT_EVENT_MODE(mode=3*)
     0x0024 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x4E)
     0x002B [0x4E] SET_ENTITY_HIDE_FLAG: Show Talking Doll (ID: 17752287/0x010EE0DF)
     0x0031 [0x80] LOAD_WAIT(entity=Talking Doll (ID: 17752287/0x010EE0DF))
     0x0036 [0x4A] LocalPlayer looks at Talking Doll (ID: 17752287/0x010EE0DF)
     0x003F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
     0x0040 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
     0x0045 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s093" with entities [LocalPlayer, LocalPlayer], work=[211*, 0*]
     0x0056 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
     0x0067 [0x2B] Talking Doll (ID: 17752287/0x010EE0DF) [10028*]:
    → "HOWDY, CONTESTANTS! I'LL BE YOUR HOST, WINK. HOW CAN I HELP YOU?"
     0x006E [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x006F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
     0x0080 [0x1C] WAIT(150* ticks)
     0x0083 [0x2B] Talking Doll (ID: 17752287/0x010EE0DF) [10029*]:
    → "SEARCHING FOR $6... SEARCHING FOR $6..."
     0x008A [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x008B [0x1C] WAIT(150* ticks)
     0x008E [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s088" with entities [LocalPlayer, LocalPlayer], work=211*
     0x009D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
     0x00AE [0x1C] WAIT(60* ticks)
     0x00B1 [0x2B] Talking Doll (ID: 17752287/0x010EE0DF) [10030*]:
    → "SORRY, CONTESTANT! THERE IS NO $3 HERE! BUT THANK YOU FOR PLAYING QUIZ DE VANA'DIEL!!!"
     0x00B8 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x00B9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
     0x00CA [0x1C] WAIT(60* ticks)
     0x00CD [0x03] Work_Zone[1] = 100*
     0x00D2 [0x46] CAMERA_CONTROL: Restore default settings
     0x00D4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
     0x00E5 [0x1B] RETURN
     0x00E6 [0x03] Work_Zone[1] = 0*
     0x00EB [0x48] [System] [10026*]:
    → "THAT IS INCORRECT! NO PARTING GIFTS FOR YOU!"
     0x00EE [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x00EF [0x1B] RETURN
```
