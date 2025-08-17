# 17818219 - Cavernous Maw

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Abyssea - Grauberg (ID: 254) |
| Block Size       | 316 bytes                    |
| Total Events     | 2                            |
| References Count | 15                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [200](#event-200)     | 0x0001       |    229 |             33 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1EE8      |        7912 |
|       1 | 0x0008      |           8 |
|       2 | 0x1EEA      |        7914 |
|       3 | 0x0001      |           1 |
|       4 | 0x0000      |           0 |
|       5 | 0x00C8      |         200 |
|       6 | 0x003C      |          60 |
|       7 | 0x0013      |          19 |
|       8 | 0xFFF7786D  |  4294408301 |
|       9 | 0xFFF46761  |  4294207329 |
|      10 | 0x7CD0      |       31952 |
|      11 | 0x07E2      |        2018 |
|      12 | 0x022A      |         554 |
|      13 | 0x00C9      |         201 |
|      14 | 0x0155      |         341 |

## String References

- **7912**: An unseen force is drawing you towards the maw.
- **7914**: Warp to [Dummy/the La Theine Plateau/the Konschtat Highlands/the Tahrongi Canyon/the Buburimu Peninsula/the Valkurm Dunes/the Jugner Forest/South Gustaberg/North Gustaberg/Xarcabard/Qufim Island]? [Proceed./Not yet.]

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

### Event 200

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 229 bytes |
| Instructions | 33        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 48 00 80 23 03  02 10 01 80 24 02 80 03    .H..#.....$...
0010: 80 04 80 25 02 00 10 04  80 00 D7 00 43 00 43 01  ...%........C.C.
0020: 42 46 01 03 01 10 03 80  45 05 80 F0 FF FF 7F F0  BF......E.......
0030: FF FF 7F 66 64 6F 31 04  80 1C 06 80 38 07 80 BA  ...fdo1.....8...
0040: F0 FF FF 7F 08 80 09 80  0A 80 0B 80 80 F0 FF FF  ................
0050: 7F 45 0C 80 F8 FF FF 7F  F8 FF FF 7F 73 31 32 39  .E..........s129
0060: 04 80 45 05 80 F0 FF FF  7F F0 FF FF 7F 66 64 69  ..E..........fdi
0070: 31 04 80 1C 06 80 45 05  80 F0 FF FF 7F F0 FF FF  1.....E.........
0080: 7F 62 6C 6F 6E 04 80 45  0D 80 F0 FF FF 7F F0 FF  .blon..E........
0090: FF 7F 62 6C 6F 6E 04 80  45 05 80 F0 FF FF 7F F0  ..blon..E.......
00A0: FF FF 7F 6F 76 6C 31 04  80 45 0E 80 F0 FF FF 7F  ...ovl1..E......
00B0: F0 FF FF 7F 77 61 72 70  04 80 29 01 F0 FF FF 7F  ....warp..).....
00C0: 05 45 05 80 F0 FF FF 7F  F0 FF FF 7F 62 6C 6F 66  .E..........blof
00D0: 04 80 46 00 01 E2 00 02  00 10 03 80 00 E2 00 01  ..F.............
00E0: E2 00 20 00 21 00                                 .. .!.          
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x48] [System] [7912*]:
    → "An unseen force is drawing you towards the maw."
  2: 0x0006 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0007 [0x03] Work_Zone[2] = 8*
  4: 0x000C [0x24] CREATE_DIALOG(message_id=7914*, default_option=1*, option_flags=0*)
    → "Warp to [Dummy/the La Theine Plateau/the Konschtat Highlands/the Tahrongi Canyon/the Buburimu Peninsula/the Valkurm Dunes/the Jugner Forest/South Gustaberg/North Gustaberg/Xarcabard/Qufim Island]? [Proceed./Not yet.]"
  5: 0x0013 [0x25] WAIT_DIALOG_SELECT()
  6: 0x0014 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00D7
  7: 0x001C [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  8: 0x001E [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  9: 0x0020 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 10: 0x0021 [0x46] CAMERA_CONTROL: Disable user control
 11: 0x0023 [0x03] Work_Zone[1] = 1*
 12: 0x0028 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 13: 0x0039 [0x1C] WAIT(60* ticks)
 14: 0x003C [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 15: 0x003F [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-558.995*, pos_z=-759.967*, pos_y=31.952*, direction=177.4°*)
 16: 0x004C [0x80] LOAD_WAIT(entity=LocalPlayer)
 17: 0x0051 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s129" with entities [EventEntity, EventEntity], work=[554*, 0*]
 18: 0x0062 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x0073 [0x1C] WAIT(60* ticks)
 20: 0x0076 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 21: 0x0087 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 22: 0x0098 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 23: 0x00A9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "warp" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 24: 0x00BA [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 25: 0x00C1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 26: 0x00D2 [0x46] CAMERA_CONTROL: Restore default settings
 27: 0x00D4 [0x01] GOTO 0x00E2
 28: 0x00D7 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00E2
 29: 0x00DF [0x01] GOTO 0x00E2

SUBROUTINE_00E2:
 30: 0x00E2 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 31: 0x00E4 [0x21] END_EVENT
 32: 0x00E5 [0x00] END_REQSTACK()
```
