# 17756220 - Seven of Diamonds

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 208 bytes                |
| Total Events     | 5                        |
| References Count | 9                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [264](#event-264)     | 0x0001       |     15 |              8 |
| [443](#event-443)     | 0x0010       |      7 |              2 |
| [390](#event-390)     | 0x0017       |    104 |             23 |
| [395](#event-395)     | 0x007F       |      6 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1E15      |        7701 |
|       1 | 0x227C      |        8828 |
|       2 | 0x227D      |        8829 |
|       3 | 0x227E      |        8830 |
|       4 | 0x0000      |           0 |
|       5 | 0x0001      |           1 |
|       6 | 0x00C8      |         200 |
|       7 | 0x0078      |         120 |
|       8 | 0x0002      |           2 |

## String References

- **7701**: oFf$26LiM-iTs! bE-yONd$26gAtE EX-trEmeLy$26dAn-GeRoUs! TuRn$26bAck$26iM-mEdiAteLy!
- **8828**: YoU$26hAVe aUthOR-iZat-iON$26FrOM$26rHinOsTEry?
- **8829**: IF$26aN Em-ERg-EncY$26liKE yOu$26SAy,$26SeVeN$26WiLL oPEn$26tHE gAtE$26fOR yOu.
- **8830**: Enter the Priming Gate? [Here we go.../Not just yet...]

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

### Event 264

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 15 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  1D 00 80 23 20 00 21 00   .....op...# .!.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=7701*)
    → "oFf$26LiM-iTs! bE-yONd$26gAtE EX-trEmeLy$26dAn-GeRoUs! TuRn$26bAck$26iM-mEdiAteLy!"
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  6: 0x000E [0x21] END_EVENT
  7: 0x000F [0x00] END_REQSTACK()
```

### Event 443

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0010  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0010 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0016 [0x00] END_REQSTACK()
```

### Event 390

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0017    |
| Data Size    | 104 bytes |
| Instructions | 23        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      1E  F0 FF FF 7F 6F 70 1D 01         .....op..
0020: 80 23 1D 02 80 23 24 03  80 04 80 04 80 25 02 00  .#...#$......%..
0030: 10 04 80 00 6B 00 42 03  01 10 05 80 45 06 80 F8  ....k.B.....E...
0040: FF FF 7F F8 FF FF 7F 66  64 6F 31 04 80 1C 07 80  .......fdo1.....
0050: 29 08 F0 FF FF 7F 3C 45  06 80 F8 FF FF 7F F8 FF  ).....<E........
0060: FF 7F 66 64 69 31 04 80  01 7B 00 02 00 10 05 80  ..fdi1...{......
0070: 00 7B 00 03 01 10 08 80  01 7B 00 20 00 21 00     .{.......{. .!. 
```

#### Opcodes

```
  0: 0x0017 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x001C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x001D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x001E [0x1D] PRINT_EVENT_MESSAGE(message_id=8828*)
    → "YoU$26hAVe aUthOR-iZat-iON$26FrOM$26rHinOsTEry?"
  4: 0x0021 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0022 [0x1D] PRINT_EVENT_MESSAGE(message_id=8829*)
    → "IF$26aN Em-ERg-EncY$26liKE yOu$26SAy,$26SeVeN$26WiLL oPEn$26tHE gAtE$26fOR yOu."
  6: 0x0025 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0026 [0x24] CREATE_DIALOG(message_id=8830*, default_option=0*, option_flags=0*)
    → "Enter the Priming Gate? [Here we go.../Not just yet...]"
  8: 0x002D [0x25] WAIT_DIALOG_SELECT()
  9: 0x002E [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x006B
 10: 0x0036 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 11: 0x0037 [0x03] Work_Zone[1] = 1*
 12: 0x003C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 13: 0x004D [0x1C] WAIT(120* ticks)
 14: 0x0050 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=LocalPlayer, tag_num=0x3C)
 15: 0x0057 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 16: 0x0068 [0x01] GOTO 0x007B
 17: 0x006B [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x007B
 18: 0x0073 [0x03] Work_Zone[1] = 2*
 19: 0x0078 [0x01] GOTO 0x007B

SUBROUTINE_007B:
 20: 0x007B [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 21: 0x007D [0x21] END_EVENT
 22: 0x007E [0x00] END_REQSTACK()
```

### Event 395

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007F  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               1E                 .
0080: F0 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x007F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0084 [0x00] END_REQSTACK()
```
