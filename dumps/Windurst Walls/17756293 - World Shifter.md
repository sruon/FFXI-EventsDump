# 17756293 - World Shifter

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 504 bytes                |
| Total Events     | 3                        |
| References Count | 30                       |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [10007](#event-10007) | 0x0001       |    297 |             80 |
| [10006](#event-10006) | 0x012A       |     55 |             15 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0064      |         100 |
|       1 | 0x1FC6      |        8134 |
|       2 | 0x1FC7      |        8135 |
|       3 | 0x1FC8      |        8136 |
|       4 | 0x1FC9      |        8137 |
|       5 | 0x0000      |           0 |
|       6 | 0x1FCA      |        8138 |
|       7 | 0x1FCB      |        8139 |
|       8 | 0x1FCC      |        8140 |
|       9 | 0x1FCD      |        8141 |
|      10 | 0x1FCE      |        8142 |
|      11 | 0x1FCF      |        8143 |
|      12 | 0x1FD0      |        8144 |
|      13 | 0x1FD1      |        8145 |
|      14 | 0x1FD2      |        8146 |
|      15 | 0x0001      |           1 |
|      16 | 0x40000000  |  1073741824 |
|      17 | 0xFFF00000  |  4293918720 |
|      18 | 0xFFFFF     |     1048575 |
|      19 | 0xFFFFFFFF  |  4294967295 |
|      20 | 0x0015      |          21 |
|      21 | 0x0013      |          19 |
|      22 | 0x000D      |          13 |
|      23 | 0x1FD9      |        8153 |
|      24 | 0x1FDA      |        8154 |
|      25 | 0x0077      |         119 |
|      26 | 0x0063      |          99 |
|      27 | 0x1FDB      |        8155 |
|      28 | 0x1FD4      |        8148 |
|      29 | 0x1FD5      |        8149 |

## String References

- **8134**: The WES (World Emigration Service) is currently taking applications for those who wish to immigrate to another World.
- **8135**: When applying, please note the following:
- **8136**: You can always cancel your emigration during the application period by talking to any of the WES agents located conveniently about Vana'diel. However, once the period is over, you will no longer be able to cancel.
- **8137**: After immigrating to another World, you will not be allowed to return to your previous World. Also, emigration is only allowed during periods when the WES is accepting applications.
- **8138**: You will be unable to choose the World to which you wish to emigrate. For more information on Worlds that we are accepting emigration applications for, please check the current PlayOnline news.
- **8139**: If your character happens to have the same name as another player in the World to which you emigrate, you will have to change your name before entering that World.
- **8140**: Emigration of characters is done one at a time.
- **8141**: If you request emigration for any of your other characters, please conduct all applications separately.
- **8142**: All items up for auction and in your Delivery Box will be lost when you emigrate. Please collect these items before moving.
- **8143**: Any items in your Mog Safe will be transported with you to the new World.
- **8144**: Any linkshells, linkpearls, and pearl sacks will be destroyed at the time of emigration. However, linkshell owners will be presented with a new, unopened linkshell.
- **8145**: Finally, all markers placed on your maps will be erased.
- **8146**: Do you wish to apply for emigration? [Yes./No.]
- **8148**: You have already submitted an application for emigration.
- **8149**: Do you wish to cancel your application? [Yes./No.]
- **8153**: Which world will you emigrate to? [I've changed my mind./Bahamut/Shiva/Titan/Ramuh/Phoenix/Carbuncle/Fenrir/Sylph/Valefor/Alexander/Leviathan/Odin/Ifrit/Diabolos/Caitsith/Quetzalcoatl/Siren/Unicorn/Gilgamesh/Ragnarok/Next page.]
- **8154**: Which world will you emigrate to? [I've changed my mind./Pandemonium/Garuda/Cerberus/Kujata/Bismarck/Seraph/Lakshmi/Asura/Midgardsormr/Fairy/Remora/Hades/Previous page.]
- **8155**: You have already submitted an application for emigration to [Bahamut/Shiva/Titan/Ramuh/Phoenix/Carbuncle/Fenrir/Sylph/Valefor/Alexander/Leviathan/Odin/Ifrit/Diabolos/Caitsith/Quetzalcoatl/Siren/Unicorn/Gilgamesh/Ragnarok/Pandemonium/Garuda/Cerberus/Kujata/Bismarck/Seraph/Lakshmi/Asura/Midgardsormr/Fairy/Remora/Hades].

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

### Event 10007

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 297 bytes |
| Instructions | 70        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    08 03 10 00 80 1E F0  FF FF 7F 1D 01 80 23 1D   .............#.
0010: 02 80 23 1D 03 80 23 1D  04 80 23 02 02 10 05 80  ..#...#...#.....
0020: 00 27 00 1D 06 80 23 1D  07 80 23 1D 08 80 23 1D  .'....#...#...#.
0030: 09 80 23 1D 0A 80 23 1D  0B 80 23 1D 0C 80 23 1D  ..#...#...#...#.
0040: 0D 80 23 24 0E 80 0F 80  05 80 25 02 00 10 0F 80  ..#$......%.....
0050: 00 5D 00 03 01 10 10 80  21 00 01 5D 00 02 02 10  .]......!..]....
0060: 0F 80 00 28 01 42 03 00  00 04 10 03 01 00 04 10  ...(.B..........
0070: 0E 00 00 11 80 0E 01 00  12 80 03 02 00 00 00 10  ................
0080: 00 00 0F 80 02 01 00 13  80 00 96 00 3C 00 00 14  ............<...
0090: 80 0F 80 01 9D 00 3D 00  00 14 80 0F 80 11 01 00  ......=.........
00A0: 15 80 3D 01 00 05 80 0F  80 02 02 00 13 80 00 BE  ..=.............
00B0: 00 3C 01 00 16 80 0F 80  01 E7 00 01 C5 00 3D 01  .<............=.
00C0: 00 16 80 0F 80 24 17 80  05 80 00 00 25 02 00 10  .....$......%...
00D0: 05 80 00 DF 00 03 01 10  10 80 21 00 01 1E 01 02  ..........!.....
00E0: 00 10 14 80 00 1E 01 24  18 80 05 80 01 00 25 02  .......$......%.
00F0: 00 10 05 80 00 01 01 03  01 10 10 80 21 00 01 0F  ............!...
0100: 01 02 00 10 16 80 00 0F  01 01 C5 00 01 0F 01 03  ................
0110: 01 10 00 10 07 01 10 19  80 21 00 01 1E 01 03 01  .........!......
0120: 10 00 10 07 01 10 1A 80  21 00                    ........!.      
```

#### Opcodes

```
  0: 0x0001 [0x08] Work_Zone[3] -= 100*
  1: 0x0006 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x000B [0x1D] PRINT_EVENT_MESSAGE(message_id=8134*)
    → "The WES (World Emigration Service) is currently taking applications for those who wish to immigrate to another World."
  3: 0x000E [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000F [0x1D] PRINT_EVENT_MESSAGE(message_id=8135*)
    → "When applying, please note the following:"
  5: 0x0012 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0013 [0x1D] PRINT_EVENT_MESSAGE(message_id=8136*)
    → "You can always cancel your emigration during the application period by talking to any of the WES agents located conveniently about Vana'diel. However, once the period is over, you will no longer be able to cancel."
  7: 0x0016 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=8137*)
    → "After immigrating to another World, you will not be allowed to return to your previous World. Also, emigration is only allowed during periods when the WES is accepting applications."
  9: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x001B [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0027
 11: 0x0023 [0x1D] PRINT_EVENT_MESSAGE(message_id=8138*)
    → "You will be unable to choose the World to which you wish to emigrate. For more information on Worlds that we are accepting emigration applications for, please check the current PlayOnline news."
 12: 0x0026 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0027 [0x1D] PRINT_EVENT_MESSAGE(message_id=8139*)
    → "If your character happens to have the same name as another player in the World to which you emigrate, you will have to change your name before entering that World."
 14: 0x002A [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x002B [0x1D] PRINT_EVENT_MESSAGE(message_id=8140*)
    → "Emigration of characters is done one at a time."
 16: 0x002E [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x002F [0x1D] PRINT_EVENT_MESSAGE(message_id=8141*)
    → "If you request emigration for any of your other characters, please conduct all applications separately."
 18: 0x0032 [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x0033 [0x1D] PRINT_EVENT_MESSAGE(message_id=8142*)
    → "All items up for auction and in your Delivery Box will be lost when you emigrate. Please collect these items before moving."
 20: 0x0036 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x0037 [0x1D] PRINT_EVENT_MESSAGE(message_id=8143*)
    → "Any items in your Mog Safe will be transported with you to the new World."
 22: 0x003A [0x23] WAIT_FOR_DIALOG_INTERACTION
 23: 0x003B [0x1D] PRINT_EVENT_MESSAGE(message_id=8144*)
    → "Any linkshells, linkpearls, and pearl sacks will be destroyed at the time of emigration. However, linkshell owners will be presented with a new, unopened linkshell."
 24: 0x003E [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x003F [0x1D] PRINT_EVENT_MESSAGE(message_id=8145*)
    → "Finally, all markers placed on your maps will be erased."
 26: 0x0042 [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x0043 [0x24] CREATE_DIALOG(message_id=8146*, default_option=1*, option_flags=0*)
    → "Do you wish to apply for emigration? [Yes./No.]"
 28: 0x004A [0x25] WAIT_DIALOG_SELECT()
 29: 0x004B [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x005D
 30: 0x0053 [0x03] Work_Zone[1] = 1073741824*
 31: 0x0058 [0x21] END_EVENT
 32: 0x0059 [0x00] END_REQSTACK()

SUBROUTINE_005D:
 33: 0x005D [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x0128
 34: 0x0065 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 35: 0x0066 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[4]
 36: 0x006B [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[4]
 37: 0x0070 [0x0E] ExtData[1]->WorkLocal[0] |= 4293918720*
 38: 0x0075 [0x0E] ExtData[1]->WorkLocal[1] |= 1048575*
 39: 0x007A [0x03] ExtData[1]->WorkLocal[2] = ExtData[1]->WorkLocal[0]
 40: 0x007F [0x10] ExtData[1]->WorkLocal[0] <<= 1*
 41: 0x0084 [0x02] IF !(ExtData[1]->WorkLocal[1] == 4294967295*) GOTO 0x0096
 42: 0x008C [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=21*, condition_work_offset=1*)
 43: 0x0093 [0x01] GOTO 0x009D
 44: 0x0096 [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=21*, condition_work_offset=1*)

SUBROUTINE_009D:
 45: 0x009D [0x11] ExtData[1]->WorkLocal[1] >>= 19*
 46: 0x00A2 [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[1], bit_index_work_offset=0*, condition_work_offset=1*)
 47: 0x00A9 [0x02] IF !(ExtData[1]->WorkLocal[2] == 4294967295*) GOTO 0x00BE
 48: 0x00B1 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[1], bit_index_work_offset=13*, condition_work_offset=1*)
 49: 0x00B8 [0x01] GOTO 0x00E7

SUBROUTINE_00C5:
 50: 0x00C5 [0x24] CREATE_DIALOG(message_id=8153*, default_option=0*, option_flags=ExtData[1]->WorkLocal[0])
    → "Which world will you emigrate to? [I've changed my mind./Bahamut/Shiva/Titan/Ramuh/Phoenix/Carbuncle/Fenrir/Sylph/Valefor/Alexander/Leviathan/Odin/Ifrit/Diabolos/Caitsith/Quetzalcoatl/Siren/Unicorn/Gilgamesh/Ragnarok/Next page.]"
 51: 0x00CC [0x25] WAIT_DIALOG_SELECT()
 52: 0x00CD [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00DF
 53: 0x00D5 [0x03] Work_Zone[1] = 1073741824*
 54: 0x00DA [0x21] END_EVENT
 55: 0x00DB [0x00] END_REQSTACK()

SUBROUTINE_00E7:
 56: 0x00E7 [0x24] CREATE_DIALOG(message_id=8154*, default_option=0*, option_flags=ExtData[1]->WorkLocal[1])
    → "Which world will you emigrate to? [I've changed my mind./Pandemonium/Garuda/Cerberus/Kujata/Bismarck/Seraph/Lakshmi/Asura/Midgardsormr/Fairy/Remora/Hades/Previous page.]"
 57: 0x00EE [0x25] WAIT_DIALOG_SELECT()
 58: 0x00EF [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0101
 59: 0x00F7 [0x03] Work_Zone[1] = 1073741824*
 60: 0x00FC [0x21] END_EVENT
 61: 0x00FD [0x00] END_REQSTACK()

SUBROUTINE_010F:
 62: 0x010F [0x03] Work_Zone[1] = Work_Zone[0]
 63: 0x0114 [0x07] Work_Zone[1] += 119*
 64: 0x0119 [0x21] END_EVENT
 65: 0x011A [0x00] END_REQSTACK()

SUBROUTINE_011E:
 66: 0x011E [0x03] Work_Zone[1] = Work_Zone[0]
 67: 0x0123 [0x07] Work_Zone[1] += 99*
 68: 0x0128 [0x21] END_EVENT
 69: 0x0129 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x005A [0x01] GOTO 0x005D
# Dead code (unreachable instructions):
     0x00BB [0x01] GOTO 0x00C5
# Dead code (unreachable instructions):
     0x00DC [0x01] GOTO 0x011E
# Dead code (unreachable instructions):
     0x00FE [0x01] GOTO 0x010F
     0x010C [0x01] GOTO 0x010F
# Dead code (unreachable instructions):
     0x011B [0x01] GOTO 0x011E
```

### Event 10006

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012A   |
| Data Size    | 55 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                08 03 10 00 80 1E            ......
0130: F0 FF FF 7F 02 02 10 0F  80 00 43 01 1D 1B 80 23  ..........C....#
0140: 01 47 01 1D 1C 80 23 24  1D 80 0F 80 05 80 25 02  .G....#$......%.
0150: 00 10 0F 80 00 5F 01 03  01 10 10 80 01 5F 01 21  ....._......._.!
0160: 00                                                .               
```

#### Opcodes

```
  0: 0x012A [0x08] Work_Zone[3] -= 100*
  1: 0x012F [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0134 [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x0143
  3: 0x013C [0x1D] PRINT_EVENT_MESSAGE(message_id=8155*)
    → "You have already submitted an application for emigration to [Bahamut/Shiva/Titan/Ramuh/Phoenix/Carbuncle/Fenrir/Sylph/Valefor/Alexander/Leviathan/Odin/Ifrit/Diabolos/Caitsith/Quetzalcoatl/Siren/Unicorn/Gilgamesh/Ragnarok/Pandemonium/Garuda/Cerberus/Kujata/Bismarck/Seraph/Lakshmi/Asura/Midgardsormr/Fairy/Remora/Hades]."
  4: 0x013F [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0140 [0x01] GOTO 0x0147
  6: 0x0143 [0x1D] PRINT_EVENT_MESSAGE(message_id=8148*)
    → "You have already submitted an application for emigration."
  7: 0x0146 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0147:
  8: 0x0147 [0x24] CREATE_DIALOG(message_id=8149*, default_option=1*, option_flags=0*)
    → "Do you wish to cancel your application? [Yes./No.]"
  9: 0x014E [0x25] WAIT_DIALOG_SELECT()
 10: 0x014F [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x015F
 11: 0x0157 [0x03] Work_Zone[1] = 1073741824*
 12: 0x015C [0x01] GOTO 0x015F

SUBROUTINE_015F:
 13: 0x015F [0x21] END_EVENT
 14: 0x0160 [0x00] END_REQSTACK()
```
