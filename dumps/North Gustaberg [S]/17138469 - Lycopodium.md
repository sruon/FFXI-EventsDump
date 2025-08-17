# 17138469 - Lycopodium

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | North Gustaberg [S] (ID: 88) |
| Block Size       | 280 bytes                    |
| Total Events     | 2                            |
| References Count | 9                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [113](#event-113)     | 0x0001       |    217 |             27 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x003C      |          60 |
|       3 | 0x0013      |          19 |
|       4 | 0x0155      |         341 |
|       5 | 0x00C9      |         201 |
|       6 | 0x001E      |          30 |
|       7 | 0x1BA4      |        7076 |
|       8 | 0x012C      |         300 |

## String References

- **7076**: Your memory is engraved with an image of your surroundings and the fragrance of flowers...

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

### Event 113

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 217 bytes |
| Instructions | 27        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 20 01 46 01 45 00  80 F0 FF FF 7F F0 FF FF   B .F.E.........
0010: 7F 66 64 6F 31 01 80 1C  02 80 38 03 80 92 01 F8  .fdo1.....8.....
0020: FF FF 7F 92 01 F0 FF FF  7F 45 04 80 F0 FF FF 7F  .........E......
0030: F0 FF FF 7F 77 70 30 32  01 80 45 00 80 F0 FF FF  ....wp02..E.....
0040: 7F F0 FF FF 7F 62 6C 6F  6E 01 80 45 05 80 F0 FF  .....blon..E....
0050: FF 7F F0 FF FF 7F 62 6C  6F 6E 01 80 45 00 80 F0  ......blon..E...
0060: FF FF 7F F0 FF FF 7F 6F  76 6C 31 01 80 45 00 80  .......ovl1..E..
0070: F0 FF FF 7F F0 FF FF 7F  66 64 69 31 01 80 1C 02  ........fdi1....
0080: 80 45 04 80 F0 FF FF 7F  F0 FF FF 7F 77 61 72 70  .E..........warp
0090: 01 80 1C 06 80 48 07 80  1C 08 80 45 00 80 F0 FF  .....H.....E....
00A0: FF 7F F0 FF FF 7F 66 64  6F 31 01 80 1C 02 80 45  ......fdo1.....E
00B0: 00 80 F0 FF FF 7F F0 FF  FF 7F 62 6C 6F 66 01 80  ..........blof..
00C0: 46 00 45 00 80 F0 FF FF  7F F0 FF FF 7F 66 64 69  F.E..........fdi
00D0: 31 01 80 1C 02 80 20 00  21 00                    1..... .!.      
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x0004 [0x46] CAMERA_CONTROL: Disable user control
  3: 0x0006 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x0017 [0x1C] WAIT(60* ticks)
  5: 0x001A [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  6: 0x001D [0x92] EventEntity->Render.Flags3 ^= 0x01
  7: 0x0023 [0x92] LocalPlayer->Render.Flags3 ^= 0x01
  8: 0x0029 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "wp02" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
  9: 0x003A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x004B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 11: 0x005C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 12: 0x006D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 13: 0x007E [0x1C] WAIT(60* ticks)
 14: 0x0081 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "warp" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 15: 0x0092 [0x1C] WAIT(30* ticks)
 16: 0x0095 [0x48] [System] [7076*]:
    → "Your memory is engraved with an image of your surroundings and the fragrance of flowers..."
 17: 0x0098 [0x1C] WAIT(300* ticks)
 18: 0x009B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x00AC [0x1C] WAIT(60* ticks)
 20: 0x00AF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 21: 0x00C0 [0x46] CAMERA_CONTROL: Restore default settings
 22: 0x00C2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 23: 0x00D3 [0x1C] WAIT(60* ticks)
 24: 0x00D6 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 25: 0x00D8 [0x21] END_EVENT
 26: 0x00D9 [0x00] END_REQSTACK()
```
