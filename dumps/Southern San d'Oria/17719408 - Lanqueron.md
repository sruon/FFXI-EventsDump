# 17719408 - Lanqueron

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Southern San d'Oria (ID: 230) |
| Block Size       | 712 bytes                     |
| Total Events     | 13                            |
| References Count | 40                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [0](#event-0)            | 0x0001       |      1 |              1 |
| [659](#event-659)        | 0x0002       |     76 |             18 |
| [850](#event-850)        | 0x004E       |    120 |             28 |
| [945](#event-945)        | 0x00C6       |     10 |              2 |
| [65535.1](#event-655351) | 0x00D0       |     15 |              5 |
| [65535.2](#event-655352) | 0x00DF       |     68 |             12 |
| [65535.3](#event-655353) | 0x0123       |     45 |              9 |
| [65535.4](#event-655354) | 0x0150       |     89 |             16 |
| [65535.5](#event-655355) | 0x01A9       |     15 |              5 |
| [65535.6](#event-655356) | 0x01B8       |     10 |              2 |
| [65535.7](#event-655357) | 0x01C2       |     15 |              5 |
| [65535.8](#event-655358) | 0x01D1       |     18 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x2100      |        8448 |
|       2 | 0x20FF      |        8447 |
|       3 | 0x0000      |           0 |
|       4 | 0x0001      |           1 |
|       5 | 0x40000000  |  1073741824 |
|       6 | 0x001E      |          30 |
|       7 | 0x2ECD      |       11981 |
|       8 | 0x2EEF      |       12015 |
|       9 | 0x2F01      |       12033 |
|      10 | 0x2EF0      |       12016 |
|      11 | 0x2EF1      |       12017 |
|      12 | 0x0060      |          96 |
|      13 | 0x000B      |          11 |
|      14 | 0xF906      |       63750 |
|      15 | 0xFFFFC4F8  |  4294952184 |
|      16 | 0x07CF      |        1999 |
|      17 | 0x0013      |          19 |
|      18 | 0x7FC6      |       32710 |
|      19 | 0xFFFF82CC  |  4294935244 |
|      20 | 0x004B      |          75 |
|      21 | 0x0027      |          39 |
|      22 | 0x4B65      |       19301 |
|      23 | 0xFFFF927C  |  4294939260 |
|      24 | 0x001D      |          29 |
|      25 | 0x000D      |          13 |
|      26 | 0xFFFFE0FB  |  4294959355 |
|      27 | 0xFFFFFCD8  |  4294966488 |
|      28 | 0x0078      |         120 |
|      29 | 0xFFFFBEF4  |  4294950644 |
|      30 | 0xFFFFD7DD  |  4294957021 |
|      31 | 0xFFFFDD9F  |  4294958495 |
|      32 | 0xFFFFA44E  |  4294943822 |
|      33 | 0x007F      |         127 |
|      34 | 0x0028      |          40 |
|      35 | 0x3192      |       12690 |
|      36 | 0xFFFFCF7D  |  4294954877 |
|      37 | 0x0025      |          37 |
|      38 | 0x2E04      |       11780 |
|      39 | 0xFFFFCBDF  |  4294953951 |

## String References

- **8447**: Send an item? [Send something./No, thanks.]
- **8448**: Parcels delivered to rooms anywhere in Vana'diel!
- **11981**: Ask if this person is the chick's owner? [Yes./No.]
- **12015**: What's this? You have a parcel for me?
- **12016**: Not a parcel, but a chocobo, you say!? Merciful Altana! My chocobo is safe, right? I thought I could take her on a walk between deliveries, but afterwards I accidentally left her with the parcels I delivered!
- **12017**: You have my utmost thanks for finding her. Let me teach you a story I often tell my chocobo...
- **12033**: Not a parcel, but a chocobo, you say? You must be mistaken. I was with my chocobo mere moments ago.

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

### Event 0

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 659

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 76 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       1E F0 FF FF 7F 6F  70 66 00 80 F8 FF FF 7F    .....opf......
0010: F8 FF FF 7F 74 6C 6B 30  1D 01 80 23 5E 69 64 6C  ....tlk0...#^idl
0020: 30 24 02 80 03 80 03 80  25 02 00 10 03 80 00 39  0$......%......9
0030: 00 03 01 10 03 80 01 49  00 02 00 10 04 80 00 49  .......I.......I
0040: 00 03 01 10 05 80 01 49  00 1C 06 80 21 00        .......I....!.  
```

#### Opcodes

```
  0: 0x0002 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0007 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0008 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0009 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=8448*)
    → "Parcels delivered to rooms anywhere in Vana'diel!"
  5: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001C [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x0021 [0x24] CREATE_DIALOG(message_id=8447*, default_option=0*, option_flags=0*)
    → "Send an item? [Send something./No, thanks.]"
  8: 0x0028 [0x25] WAIT_DIALOG_SELECT()
  9: 0x0029 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0039
 10: 0x0031 [0x03] Work_Zone[1] = 0*
 11: 0x0036 [0x01] GOTO 0x0049
 12: 0x0039 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0049
 13: 0x0041 [0x03] Work_Zone[1] = 1073741824*
 14: 0x0046 [0x01] GOTO 0x0049

SUBROUTINE_0049:
 15: 0x0049 [0x1C] WAIT(30* ticks)
 16: 0x004C [0x21] END_EVENT
 17: 0x004D [0x00] END_REQSTACK()
```

### Event 850

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x004E    |
| Data Size    | 120 bytes |
| Instructions | 28        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            42 03                B.
0050: 01 10 03 80 24 07 80 04  80 03 80 25 02 00 10 03  ....$......%....
0060: 80 00 C4 00 1E F0 FF FF  7F 1C 06 80 03 01 10 04  ................
0070: 80 43 00 43 01 02 02 10  03 80 00 97 00 1D 08 80  .C.C............
0080: 23 66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30  #f..........tlk0
0090: 1D 09 80 23 01 C1 00 1D  08 80 23 66 00 80 F8 FF  ...#......#f....
00A0: FF 7F F8 FF FF 7F 74 6C  6B 30 1D 0A 80 23 66 00  ......tlk0...#f.
00B0: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 31 1D 0B 80  .........tlk1...
00C0: 23 01 C4 00 21 00                                 #...!.          
```

#### Opcodes

```
  0: 0x004E [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x004F [0x03] Work_Zone[1] = 0*
  2: 0x0054 [0x24] CREATE_DIALOG(message_id=11981*, default_option=1*, option_flags=0*)
    → "Ask if this person is the chick's owner? [Yes./No.]"
  3: 0x005B [0x25] WAIT_DIALOG_SELECT()
  4: 0x005C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00C4
  5: 0x0064 [0x1E] EventEntity looks at LocalPlayer and starts talking
  6: 0x0069 [0x1C] WAIT(30* ticks)
  7: 0x006C [0x03] Work_Zone[1] = 1*
  8: 0x0071 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  9: 0x0073 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 10: 0x0075 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0097
 11: 0x007D [0x1D] PRINT_EVENT_MESSAGE(message_id=12015*)
    → "What's this? You have a parcel for me?"
 12: 0x0080 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0081 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
 14: 0x0090 [0x1D] PRINT_EVENT_MESSAGE(message_id=12033*)
    → "Not a parcel, but a chocobo, you say? You must be mistaken. I was with my chocobo mere moments ago."
 15: 0x0093 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0094 [0x01] GOTO 0x00C1
 17: 0x0097 [0x1D] PRINT_EVENT_MESSAGE(message_id=12015*)
    → "What's this? You have a parcel for me?"
 18: 0x009A [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x009B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
 20: 0x00AA [0x1D] PRINT_EVENT_MESSAGE(message_id=12016*)
    → "Not a parcel, but a chocobo, you say!? Merciful Altana! My chocobo is safe, right? I thought I could take her on a walk between deliveries, but afterwards I accidentally left her with the parcels I delivered!"
 21: 0x00AD [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x00AE [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
 23: 0x00BD [0x1D] PRINT_EVENT_MESSAGE(message_id=12017*)
    → "You have my utmost thanks for finding her. Let me teach you a story I often tell my chocobo..."
 24: 0x00C0 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_00C1:
 25: 0x00C1 [0x01] GOTO 0x00C4

SUBROUTINE_00C4:
 26: 0x00C4 [0x21] END_EVENT
 27: 0x00C5 [0x00] END_REQSTACK()
```

### Event 945

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C6   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                   6C F8  FF FF 7F 0C 80 04 80 00        l.........
```

#### Opcodes

```
  0: 0x00C6 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=96*, fade_time=1*)
  1: 0x00CF [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D0   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0: 32 0D 80 1F 00 0E 80 0F  80 10 80 1F 01 6F 00     2............o. 
```

#### Opcodes

```
  0: 0x00D0 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x00D3 [0x1F] MOVE_ENTITY: EventEntity moves to X=63.750*, Z=-15.112*, Y=1.999*
  2: 0x00DB [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00DD [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00DE [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DF   |
| Data Size    | 68 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                               32                 2
00E0: 11 80 1F 00 12 80 13 80  10 80 1F 01 6F 1E 3D 60  ............o.=`
00F0: 0E 01 6F 76 F8 FF FF 7F  4A 3D 60 0E 01 F8 FF FF  ..ov....J=`.....
0100: 7F 5B 14 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30  .[..........tlk0
0110: 1C 06 80 5B 14 80 3D 60  0E 01 3D 60 0E 01 74 68  ...[..=`..=`..th
0120: 6B 30 00                                          k0.             
```

#### Opcodes

```
  0: 0x00DF [0x32] ExtData[1]->MainSpeed = 19* * 0.1
  1: 0x00E2 [0x1F] MOVE_ENTITY: EventEntity moves to X=32.710*, Z=-32.052*, Y=1.999*
  2: 0x00EA [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00EC [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00ED [0x1E] EventEntity looks at Authere (ID: 17719357/0x010E603D) and starts talking
  5: 0x00F2 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x00F3 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  7: 0x00F8 [0x4A] Authere (ID: 17719357/0x010E603D) looks at EventEntity
  8: 0x0101 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=75*
  9: 0x0110 [0x1C] WAIT(30* ticks)
 10: 0x0113 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk0" with entities [Authere (ID: 17719357/0x010E603D), Authere (ID: 17719357/0x010E603D)], work=75*
 11: 0x0122 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0123   |
| Data Size    | 45 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:          32 15 80 1F 00  16 80 17 80 10 80 1F 01     2............
0130: 6F 4A 72 60 0E 01 F8 FF  FF 7F 6F 76 72 60 0E 01  oJr`......ovr`..
0140: 66 18 80 72 60 0E 01 72  60 0E 01 74 77 61 30 00  f..r`..r`..twa0.
```

#### Opcodes

```
  0: 0x0123 [0x32] ExtData[1]->MainSpeed = 39* * 0.1
  1: 0x0126 [0x1F] MOVE_ENTITY: EventEntity moves to X=19.301*, Z=-28.036*, Y=1.999*
  2: 0x012E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0130 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0131 [0x4A] Vaquelage (ID: 17719410/0x010E6072) looks at EventEntity
  5: 0x013A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x013B [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Vaquelage (ID: 17719410/0x010E6072) Render.Flags0 and Render.Flags3 conditions are met
  7: 0x0140 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "twa0" with entities [Vaquelage (ID: 17719410/0x010E6072), Vaquelage (ID: 17719410/0x010E6072)], work=29*
  8: 0x014F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0150   |
| Data Size    | 89 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150: 32 19 80 1F 00 1A 80 1B  80 10 80 1F 01 6F 79 00  2............oy.
0160: F8 FF FF 7F 7E 60 0E 01  4A 7E 60 0E 01 F8 FF FF  ....~`..J~`.....
0170: 7F 6F 76 7E 60 0E 01 5B  15 80 7E 60 0E 01 7E 60  .ov~`..[..~`..~`
0180: 0E 01 74 6C 6B 30 1C 1C  80 5B 15 80 7E 60 0E 01  ..tlk0...[..~`..
0190: 7E 60 0E 01 74 6C 6B 31  7B F8 FF FF 7F 1F 00 1D  ~`..tlk1{.......
01A0: 80 1E 80 10 80 1F 01 6F  00                       .......o.       
```

#### Opcodes

```
  0: 0x0150 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0153 [0x1F] MOVE_ENTITY: EventEntity moves to X=-7.941*, Z=-0.808*, Y=1.999*
  2: 0x015B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x015D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x015E [0x79] EventEntity looks at Ailevia (ID: 17719422/0x010E607E) (Basic look)
  5: 0x0168 [0x4A] Ailevia (ID: 17719422/0x010E607E) looks at EventEntity
  6: 0x0171 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x0172 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Ailevia (ID: 17719422/0x010E607E) Render.Flags0 and Render.Flags3 conditions are met
  8: 0x0177 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Ailevia (ID: 17719422/0x010E607E), Ailevia (ID: 17719422/0x010E607E)], work=39*
  9: 0x0186 [0x1C] WAIT(120* ticks)
 10: 0x0189 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [Ailevia (ID: 17719422/0x010E607E), Ailevia (ID: 17719422/0x010E607E)], work=39*
 11: 0x0198 [0x7B] EventEntity stops talking
 12: 0x019D [0x1F] MOVE_ENTITY: EventEntity moves to X=-16.652*, Z=-10.275*, Y=1.999*
 13: 0x01A5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 14: 0x01A7 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 15: 0x01A8 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01A9   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                             32 0D 80 1F 00 1F 80           2......
01B0: 20 80 10 80 1F 01 6F 00                            .....o.        
```

#### Opcodes

```
  0: 0x01A9 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x01AC [0x1F] MOVE_ENTITY: EventEntity moves to X=-8.801*, Z=-23.474*, Y=1.999*
  2: 0x01B4 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01B6 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x01B7 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01B8   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                          6C F8 FF FF 7F 21 80 04          l....!..
01C0: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x01B8 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=127*, fade_time=1*)
  1: 0x01C1 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01C2   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:       32 22 80 1F 00 23  80 24 80 10 80 1F 01 6F    2"...#.$.....o
01D0: 00                                                .               
```

#### Opcodes

```
  0: 0x01C2 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x01C5 [0x1F] MOVE_ENTITY: EventEntity moves to X=12.690*, Z=-12.419*, Y=1.999*
  2: 0x01CD [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01CF [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x01D0 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01D1   |
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:    1C 06 80 32 25 80 1F  00 26 80 27 80 10 80 1F   ...2%...&.'....
01E0: 01 6F 00                                          .o.             
```

#### Opcodes

```
  0: 0x01D1 [0x1C] WAIT(30* ticks)
  1: 0x01D4 [0x32] ExtData[1]->MainSpeed = 37* * 0.1
  2: 0x01D7 [0x1F] MOVE_ENTITY: EventEntity moves to X=11.780*, Z=-13.345*, Y=1.999*
  3: 0x01DF [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x01E1 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x01E2 [0x00] END_REQSTACK()
```
