# 17752278 - DoorAcolyte Hostel

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 332 bytes                 |
| Total Events     | 2                         |
| References Count | 14                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [807](#event-807)     | 0x0001       |    248 |             44 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2729      |       10025 |
|       1 | 0x0001      |           1 |
|       2 | 0x272B      |       10027 |
|       3 | 0x00C8      |         200 |
|       4 | 0x0000      |           0 |
|       5 | 0x003C      |          60 |
|       6 | 0x0003      |           3 |
|       7 | 0x00D3      |         211 |
|       8 | 0x272C      |       10028 |
|       9 | 0x0096      |         150 |
|      10 | 0x272D      |       10029 |
|      11 | 0x272E      |       10030 |
|      12 | 0x0064      |         100 |
|      13 | 0x272A      |       10026 |

## String References

- **10025**: ARE YOU READY FOR THE QUIZ DE VANA'DIEL?
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

### Event 807

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 248 bytes |
| Instructions | 7         |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 48 00 80 23 13 03  00 01 80 20 00 21 00 42   BH..#..... .!.B
0010: 46 01 48 02 80 23 45 03  80 F8 FF FF 7F F8 FF FF  F.H..#E.........
0020: 7F 66 64 6F 31 04 80 1C  05 80 38 06 80 29 0B F0  .fdo1.....8..)..
0030: FF FF 7F 4B 4E 00 DF E0  0E 01 80 DF E0 0E 01 4A  ...KN..........J
0040: F0 FF FF 7F DF E0 0E 01  6F 76 F0 FF FF 7F 45 07  ........ov....E.
0050: 80 F0 FF FF 7F F0 FF FF  7F 73 30 39 30 04 80 45  .........s090..E
0060: 03 80 F8 FF FF 7F F8 FF  FF 7F 66 64 69 31 04 80  ..........fdi1..
0070: 2B DF E0 0E 01 08 80 23  45 03 80 F8 FF FF 7F F8  +......#E.......
0080: FF FF 7F 66 64 6F 31 04  80 1C 09 80 2B DF E0 0E  ...fdo1.....+...
0090: 01 0A 80 23 1C 09 80 55  07 80 F0 FF FF 7F F0 FF  ...#...U........
00A0: FF 7F 73 30 38 38 45 03  80 F8 FF FF 7F F8 FF FF  ..s088E.........
00B0: 7F 66 64 69 31 04 80 1C  05 80 2B DF E0 0E 01 0B  .fdi1.....+.....
00C0: 80 23 45 03 80 F8 FF FF  7F F8 FF FF 7F 66 64 6F  .#E..........fdo
00D0: 31 04 80 1C 05 80 03 01  10 0C 80 46 00 45 03 80  1..........F.E..
00E0: F8 FF FF 7F F8 FF FF 7F  66 64 69 31 04 80 1B 03  ........fdi1....
00F0: 01 10 04 80 48 0D 80 23  1B                       ....H..#.       
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x48] [System] [10025*]:
    → "ARE YOU READY FOR THE QUIZ DE VANA'DIEL?"
  2: 0x0005 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0006 [0x13] ExtData[1]->WorkLocal[3] = rand() % 1*
  4: 0x000B [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  5: 0x000D [0x21] END_EVENT
  6: 0x000E [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x000F [0x42] SET_CLI_EVENT_CANCEL_DATA()
     0x0010 [0x46] CAMERA_CONTROL: Disable user control
     0x0012 [0x48] [System] [10027*]:
    → "YOU ARE RIGHT!"
     0x0015 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0016 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
     0x0027 [0x1C] WAIT(60* ticks)
     0x002A [0x38] SET_CLIENT_EVENT_MODE(mode=3*)
     0x002D [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x4B)
     0x0034 [0x4E] SET_ENTITY_HIDE_FLAG: Show Talking Doll (ID: 17752287/0x010EE0DF)
     0x003A [0x80] LOAD_WAIT(entity=Talking Doll (ID: 17752287/0x010EE0DF))
     0x003F [0x4A] LocalPlayer looks at Talking Doll (ID: 17752287/0x010EE0DF)
     0x0048 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
     0x0049 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
     0x004E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s090" with entities [LocalPlayer, LocalPlayer], work=[211*, 0*]
     0x005F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
     0x0070 [0x2B] Talking Doll (ID: 17752287/0x010EE0DF) [10028*]:
    → "HOWDY, CONTESTANTS! I'LL BE YOUR HOST, WINK. HOW CAN I HELP YOU?"
     0x0077 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0078 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
     0x0089 [0x1C] WAIT(150* ticks)
     0x008C [0x2B] Talking Doll (ID: 17752287/0x010EE0DF) [10029*]:
    → "SEARCHING FOR $6... SEARCHING FOR $6..."
     0x0093 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0094 [0x1C] WAIT(150* ticks)
     0x0097 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s088" with entities [LocalPlayer, LocalPlayer], work=211*
     0x00A6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
     0x00B7 [0x1C] WAIT(60* ticks)
     0x00BA [0x2B] Talking Doll (ID: 17752287/0x010EE0DF) [10030*]:
    → "SORRY, CONTESTANT! THERE IS NO $3 HERE! BUT THANK YOU FOR PLAYING QUIZ DE VANA'DIEL!!!"
     0x00C1 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x00C2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
     0x00D3 [0x1C] WAIT(60* ticks)
     0x00D6 [0x03] Work_Zone[1] = 100*
     0x00DB [0x46] CAMERA_CONTROL: Restore default settings
     0x00DD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
     0x00EE [0x1B] RETURN
     0x00EF [0x03] Work_Zone[1] = 0*
     0x00F4 [0x48] [System] [10026*]:
    → "THAT IS INCORRECT! NO PARTING GIFTS FOR YOU!"
     0x00F7 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x00F8 [0x1B] RETURN
```
