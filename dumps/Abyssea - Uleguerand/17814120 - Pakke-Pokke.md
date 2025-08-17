# 17814120 - Pakke-Pokke

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Abyssea - Uleguerand (ID: 253) |
| Block Size       | 308 bytes                      |
| Total Events     | 2                              |
| References Count | 16                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [347](#event-347)     | 0x0001       |    216 |             48 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1F79      |        8057 |
|       1 | 0x1F7A      |        8058 |
|       2 | 0x0000      |           0 |
|       3 | 0x0031      |          49 |
|       4 | 0x1F7B      |        8059 |
|       5 | 0x1F7C      |        8060 |
|       6 | 0x1F7D      |        8061 |
|       7 | 0x0001      |           1 |
|       8 | 0x1F7E      |        8062 |
|       9 | 0x1F7F      |        8063 |
|      10 | 0x0002      |           2 |
|      11 | 0x1F80      |        8064 |
|      12 | 0x1F81      |        8065 |
|      13 | 0x0003      |           3 |
|      14 | 0x0004      |           4 |
|      15 | 0x1F82      |        8066 |

## String References

- **8057**: Oh, hullo there! I justaru picked up some incredibly valuable-waluable combat tips from Prince Trion himself. I can share this knowledge with you, if you wish.
- **8058**: Ask something? [About weak points./About reinforcements./About killing blows./Nothing for now.]
- **8059**: Prince Trion says that the fiends possess indi-windividual weaknesses. Take advantage of these, and you may deprive them of their most potentaru attacks, or even stop them dead in their tracky-wacks.
- **8060**: Of course, uncovering a certain creature's weak pointaru is easier said than done...
- **8061**: Is there anything else you'd care to hear?
- **8062**: Prince Trion says we must be wary when battling the fiends for too long in a single-wingle location. That they'll quickly call their friends, and those friends will be nasty enough to put your original foes to shame.
- **8063**: Fortunately, it appears these fearsome fellows have bettaru things to do than to pick on adventurers beneath their stature. If you find yourself intimi-wimidated, just leave them alone, and they'll do you the same favor.
- **8064**: Prince Trion says that when you fell a fiend, your visitant glow will take on different hues depending on how you strike the killing-willing blow.
- **8065**: Sadly, he didn't go into detail, so you'll just have to experimentaru for yourself.
- **8066**: Oh, did you hear him yourself? His voice does carry-warry quite far...

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

### Event 347

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 216 bytes |
| Instructions | 19        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  1D 00 80 23 24 01 80 02   .....op...#$...
0010: 80 02 80 25 02 00 10 02  80 00 4C 00 66 03 80 68  ...%......L.f..h
0020: D2 0F 01 68 D2 0F 01 74  6C 6B 30 1D 04 80 23 1D  ...h...tlk0...#.
0030: 05 80 23 1D 06 80 23 66  03 80 68 D2 0F 01 68 D2  ..#...#f..h...h.
0040: 0F 01 74 6C 6B 31 01 0C  00 01 D7 00 02 00 10 07  ..tlk1..........
0050: 80 00 84 00 66 03 80 68  D2 0F 01 68 D2 0F 01 74  ....f..h...h...t
0060: 6C 6B 30 1D 08 80 23 1D  09 80 23 1D 06 80 23 66  lk0...#...#...#f
0070: 03 80 68 D2 0F 01 68 D2  0F 01 74 6C 6B 31 01 0C  ..h...h...tlk1..
0080: 00 01 D7 00 02 00 10 0A  80 00 BC 00 66 03 80 68  ............f..h
0090: D2 0F 01 68 D2 0F 01 74  6C 6B 30 1D 0B 80 23 1D  ...h...tlk0...#.
00A0: 0C 80 23 1D 06 80 23 66  03 80 68 D2 0F 01 68 D2  ..#...#f..h...h.
00B0: 0F 01 74 6C 6B 31 01 0C  00 01 D7 00 02 00 10 0D  ..tlk1..........
00C0: 80 00 D7 00 6E 68 D2 0F  01 0E 80 99 68 D2 0F 01  ....nh......h...
00D0: 1D 0F 80 23 01 D7 00 21  00                       ...#...!.       
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=8057*)
    → "Oh, hullo there! I justaru picked up some incredibly valuable-waluable combat tips from Prince Trion himself. I can share this knowledge with you, if you wish."
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x24] CREATE_DIALOG(message_id=8058*, default_option=0*, option_flags=0*)
    → "Ask something? [About weak points./About reinforcements./About killing blows./Nothing for now.]"
  6: 0x0013 [0x25] WAIT_DIALOG_SELECT()
  7: 0x0014 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x004C
  8: 0x001C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Pakke-Pokke (ID: 17814120/0x010FD268), Pakke-Pokke (ID: 17814120/0x010FD268)], work=49*
  9: 0x002B [0x1D] PRINT_EVENT_MESSAGE(message_id=8059*)
    → "Prince Trion says that the fiends possess indi-windividual weaknesses. Take advantage of these, and you may deprive them of their most potentaru attacks, or even stop them dead in their tracky-wacks."
 10: 0x002E [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x002F [0x1D] PRINT_EVENT_MESSAGE(message_id=8060*)
    → "Of course, uncovering a certain creature's weak pointaru is easier said than done..."
 12: 0x0032 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0033 [0x1D] PRINT_EVENT_MESSAGE(message_id=8061*)
    → "Is there anything else you'd care to hear?"
 14: 0x0036 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0037 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Pakke-Pokke (ID: 17814120/0x010FD268), Pakke-Pokke (ID: 17814120/0x010FD268)], work=49*
 16: 0x0046 [0x01] GOTO 0x000C

SUBROUTINE_00D7:
 17: 0x00D7 [0x21] END_EVENT
 18: 0x00D8 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0049 [0x01] GOTO 0x00D7
     0x0081 [0x01] GOTO 0x00D7
     0x00B9 [0x01] GOTO 0x00D7
```
