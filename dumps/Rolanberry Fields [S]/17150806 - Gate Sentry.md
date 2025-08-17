# 17150806 - Gate Sentry

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Rolanberry Fields [S] (ID: 91) |
| Block Size       | 428 bytes                      |
| Total Events     | 6                              |
| References Count | 21                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     11 |              7 |
| [253](#event-253)        | 0x000C       |    257 |             82 |
| [65535.2](#event-655352) | 0x010D       |     11 |              7 |
| [65535.3](#event-655353) | 0x0118       |     11 |              7 |
| [65535.4](#event-655354) | 0x0123       |     11 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1E73      |        7795 |
|       1 | 0x0001      |           1 |
|       2 | 0x1E78      |        7800 |
|       3 | 0x001E      |          30 |
|       4 | 0x0002      |           2 |
|       5 | 0x1E77      |        7799 |
|       6 | 0x0003      |           3 |
|       7 | 0x1E7D      |        7805 |
|       8 | 0x0004      |           4 |
|       9 | 0x0000      |           0 |
|      10 | 0x1E72      |        7794 |
|      11 | 0x1E74      |        7796 |
|      12 | 0x1E75      |        7797 |
|      13 | 0x1E76      |        7798 |
|      14 | 0x0005      |           5 |
|      15 | 0x1E7C      |        7804 |
|      16 | 0x000A      |          10 |
|      17 | 0x1E90      |        7824 |
|      18 | 0x1E91      |        7825 |
|      19 | 0x000B      |          11 |
|      20 | 0x1E92      |        7826 |

## String References

- **7794**: These are the supplies you are to deliver to the stronghold in this area.
- **7795**: The supply unit carrying rations and munitions to our stronghold in this area was attacked en route, and forced to abandon the cargo. You are to locate the supplies and deliver them to their final destination.
- **7796**: Some of the items are raw and will spoil if not delivered immediately. You must hurry.
- **7797**: Some of the items are very delicate and will be destroyed if you are not careful. Avoid all confrontation with the enemy.
- **7798**: Now move out.
- **7799**: What are you waiting for, <Player>!? Move out!
- **7800**: This is an Allied Checkpoint Garrison.
- **7804**: Alright, <Player>. The reinforcements are ready to be escorted to the stronghold in this area.
- **7805**: Welcome, <Player>. The troops you are to guide to the stronghold haven't arrived yet. Please wait a little longer.
- **7824**: About time you showed up, soldier. This here's the shipment of materials you'll be transporting.
- **7825**: I suspect you've already been briefed, but this is some volatile, dangerous stuff. But you signed up for this mission, so we're counting on you to deliver it to the stronghold before its power dissipates.
- **7826**: You'd best deliver that to the stronghold while it still packs some oomph.

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 11 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 42 1D 00 80 23  20 00 21 00                .B...# .!.    
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x1D] PRINT_EVENT_MESSAGE(message_id=7795*)
    → "The supply unit carrying rations and munitions to our stronghold in this area was attacked en route, and forced to abandon the cargo. You are to locate the supplies and deliver them to their final destination."
  3: 0x0007 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0008 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  5: 0x000A [0x21] END_EVENT
  6: 0x000B [0x00] END_REQSTACK()
```

### Event 253

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x000C    |
| Data Size    | 257 bytes |
| Instructions | 82        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      20 01 42 03               .B.
0010: 00 00 02 10 03 01 00 03  10 03 01 10 01 80 02 01  ................
0020: 00 01 80 80 37 00 1E F0  FF FF 7F 6F 70 1D 02 80  ....7......op...
0030: 23 1C 03 80 01 09 01 02  01 00 04 80 80 50 00 1E  #............P..
0040: F0 FF FF 7F 6F 70 1D 05  80 23 1C 03 80 01 09 01  ....op...#......
0050: 02 01 00 06 80 80 69 00  1E F0 FF FF 7F 6F 70 1D  ......i......op.
0060: 07 80 23 1C 03 80 01 09  01 02 01 00 08 80 80 AC  ..#.............
0070: 00 1E F0 FF FF 7F 6F 70  3E 00 00 09 80 86 00 1D  ......op>.......
0080: 00 80 23 01 8A 00 1D 0A  80 23 3E 00 00 01 80 95  ..#......#>.....
0090: 00 1D 0B 80 23 3E 00 00  04 80 A0 00 1D 0C 80 23  ....#>.........#
00A0: 1D 0D 80 23 03 01 10 01  80 01 09 01 02 01 00 0E  ...#............
00B0: 80 80 CA 00 1E F0 FF FF  7F 6F 70 1D 0F 80 23 1C  .........op...#.
00C0: 03 80 03 01 10 04 80 01  09 01 02 01 00 10 80 80  ................
00D0: F0 00 1E F0 FF FF 7F 6F  70 1D 11 80 23 1D 12 80  .......op...#...
00E0: 23 1D 0D 80 23 1C 03 80  03 01 10 06 80 01 09 01  #...#...........
00F0: 02 01 00 13 80 80 09 01  1E F0 FF FF 7F 6F 70 1D  .............op.
0100: 14 80 23 1C 03 80 01 09  01 20 00 21 00           ..#...... .!.   
```

#### Opcodes

```
  0: 0x000C [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x000E [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x000F [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  3: 0x0014 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[3]
  4: 0x0019 [0x03] Work_Zone[1] = 1*
  5: 0x001E [0x02] IF !(ExtData[1]->WorkLocal[1] == 1*) GOTO 0x0037
  6: 0x0026 [0x1E] EventEntity looks at LocalPlayer and starts talking
  7: 0x002B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x002C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  9: 0x002D [0x1D] PRINT_EVENT_MESSAGE(message_id=7800*)
    → "This is an Allied Checkpoint Garrison."
 10: 0x0030 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0031 [0x1C] WAIT(30* ticks)
 12: 0x0034 [0x01] GOTO 0x0109
 13: 0x0037 [0x02] IF !(ExtData[1]->WorkLocal[1] == 2*) GOTO 0x0050
 14: 0x003F [0x1E] EventEntity looks at LocalPlayer and starts talking
 15: 0x0044 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 16: 0x0045 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 17: 0x0046 [0x1D] PRINT_EVENT_MESSAGE(message_id=7799*)
    → "What are you waiting for, <Player>!? Move out!"
 18: 0x0049 [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x004A [0x1C] WAIT(30* ticks)
 20: 0x004D [0x01] GOTO 0x0109
 21: 0x0050 [0x02] IF !(ExtData[1]->WorkLocal[1] == 3*) GOTO 0x0069
 22: 0x0058 [0x1E] EventEntity looks at LocalPlayer and starts talking
 23: 0x005D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 24: 0x005E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 25: 0x005F [0x1D] PRINT_EVENT_MESSAGE(message_id=7805*)
    → "Welcome, <Player>. The troops you are to guide to the stronghold haven't arrived yet. Please wait a little longer."
 26: 0x0062 [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x0063 [0x1C] WAIT(30* ticks)
 28: 0x0066 [0x01] GOTO 0x0109
 29: 0x0069 [0x02] IF !(ExtData[1]->WorkLocal[1] == 4*) GOTO 0x00AC
 30: 0x0071 [0x1E] EventEntity looks at LocalPlayer and starts talking
 31: 0x0076 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 32: 0x0077 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 33: 0x0078 [0x3E] IF !(ExtData[1]->WorkLocal[0] bit 0*) GOTO 0x0086
 34: 0x007F [0x1D] PRINT_EVENT_MESSAGE(message_id=7795*)
    → "The supply unit carrying rations and munitions to our stronghold in this area was attacked en route, and forced to abandon the cargo. You are to locate the supplies and deliver them to their final destination."
 35: 0x0082 [0x23] WAIT_FOR_DIALOG_INTERACTION
 36: 0x0083 [0x01] GOTO 0x008A
 37: 0x0086 [0x1D] PRINT_EVENT_MESSAGE(message_id=7794*)
    → "These are the supplies you are to deliver to the stronghold in this area."
 38: 0x0089 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_008A:
 39: 0x008A [0x3E] IF !(ExtData[1]->WorkLocal[0] bit 1*) GOTO 0x0095
 40: 0x0091 [0x1D] PRINT_EVENT_MESSAGE(message_id=7796*)
    → "Some of the items are raw and will spoil if not delivered immediately. You must hurry."
 41: 0x0094 [0x23] WAIT_FOR_DIALOG_INTERACTION
 42: 0x0095 [0x3E] IF !(ExtData[1]->WorkLocal[0] bit 2*) GOTO 0x00A0
 43: 0x009C [0x1D] PRINT_EVENT_MESSAGE(message_id=7797*)
    → "Some of the items are very delicate and will be destroyed if you are not careful. Avoid all confrontation with the enemy."
 44: 0x009F [0x23] WAIT_FOR_DIALOG_INTERACTION
 45: 0x00A0 [0x1D] PRINT_EVENT_MESSAGE(message_id=7798*)
    → "Now move out."
 46: 0x00A3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 47: 0x00A4 [0x03] Work_Zone[1] = 1*
 48: 0x00A9 [0x01] GOTO 0x0109
 49: 0x00AC [0x02] IF !(ExtData[1]->WorkLocal[1] == 5*) GOTO 0x00CA
 50: 0x00B4 [0x1E] EventEntity looks at LocalPlayer and starts talking
 51: 0x00B9 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 52: 0x00BA [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 53: 0x00BB [0x1D] PRINT_EVENT_MESSAGE(message_id=7804*)
    → "Alright, <Player>. The reinforcements are ready to be escorted to the stronghold in this area."
 54: 0x00BE [0x23] WAIT_FOR_DIALOG_INTERACTION
 55: 0x00BF [0x1C] WAIT(30* ticks)
 56: 0x00C2 [0x03] Work_Zone[1] = 2*
 57: 0x00C7 [0x01] GOTO 0x0109
 58: 0x00CA [0x02] IF !(ExtData[1]->WorkLocal[1] == 10*) GOTO 0x00F0
 59: 0x00D2 [0x1E] EventEntity looks at LocalPlayer and starts talking
 60: 0x00D7 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 61: 0x00D8 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 62: 0x00D9 [0x1D] PRINT_EVENT_MESSAGE(message_id=7824*)
    → "About time you showed up, soldier. This here's the shipment of materials you'll be transporting."
 63: 0x00DC [0x23] WAIT_FOR_DIALOG_INTERACTION
 64: 0x00DD [0x1D] PRINT_EVENT_MESSAGE(message_id=7825*)
    → "I suspect you've already been briefed, but this is some volatile, dangerous stuff. But you signed up for this mission, so we're counting on you to deliver it to the stronghold before its power dissipates."
 65: 0x00E0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 66: 0x00E1 [0x1D] PRINT_EVENT_MESSAGE(message_id=7798*)
    → "Now move out."
 67: 0x00E4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 68: 0x00E5 [0x1C] WAIT(30* ticks)
 69: 0x00E8 [0x03] Work_Zone[1] = 3*
 70: 0x00ED [0x01] GOTO 0x0109
 71: 0x00F0 [0x02] IF !(ExtData[1]->WorkLocal[1] == 11*) GOTO 0x0109
 72: 0x00F8 [0x1E] EventEntity looks at LocalPlayer and starts talking
 73: 0x00FD [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 74: 0x00FE [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 75: 0x00FF [0x1D] PRINT_EVENT_MESSAGE(message_id=7826*)
    → "You'd best deliver that to the stronghold while it still packs some oomph."
 76: 0x0102 [0x23] WAIT_FOR_DIALOG_INTERACTION
 77: 0x0103 [0x1C] WAIT(30* ticks)
 78: 0x0106 [0x01] GOTO 0x0109

SUBROUTINE_0109:
 79: 0x0109 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 80: 0x010B [0x21] END_EVENT
 81: 0x010C [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010D   |
| Data Size    | 11 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                         20 01 42                .B
0110: 1D 0C 80 23 20 00 21 00                           ...# .!.        
```

#### Opcodes

```
  0: 0x010D [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x010F [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0110 [0x1D] PRINT_EVENT_MESSAGE(message_id=7797*)
    → "Some of the items are very delicate and will be destroyed if you are not careful. Avoid all confrontation with the enemy."
  3: 0x0113 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0114 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  5: 0x0116 [0x21] END_EVENT
  6: 0x0117 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0118   |
| Data Size    | 11 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                          20 01 42 1D 0B 80 23 20           .B...# 
0120: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0118 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x011A [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x011B [0x1D] PRINT_EVENT_MESSAGE(message_id=7796*)
    → "Some of the items are raw and will spoil if not delivered immediately. You must hurry."
  3: 0x011E [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x011F [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  5: 0x0121 [0x21] END_EVENT
  6: 0x0122 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0123   |
| Data Size    | 11 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:          20 01 42 1D 0D  80 23 20 00 21 00            .B...# .!.  
```

#### Opcodes

```
  0: 0x0123 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0125 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0126 [0x1D] PRINT_EVENT_MESSAGE(message_id=7798*)
    → "Now move out."
  3: 0x0129 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x012A [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  5: 0x012C [0x21] END_EVENT
  6: 0x012D [0x00] END_REQSTACK()
```
