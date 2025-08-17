# 16793993 - Clamming Point

## Common Data

| Field            | Value              |
|------------------|--------------------|
| Zone             | Bibiki Bay (ID: 4) |
| Block Size       | 120 bytes          |
| Total Events     | 2                  |
| References Count | 5                  |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [22](#event-22)       | 0x0001       |     74 |             17 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1C62      |        7266 |
|       1 | 0x1C63      |        7267 |
|       2 | 0x0000      |           0 |
|       3 | 0x0027      |          39 |
|       4 | 0x0001      |           1 |

## String References

- **7266**: The area is littered with pieces of broken seashells.
- **7267**: Dig here? [Yep./Nope.]

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

### Event 22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 74 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4A F0 FF FF 7F 89 41  00 01 48 00 80 23 24 01   J.....A..H..#$.
0010: 80 02 80 02 80 25 02 00  10 02 80 00 49 00 42 43  .....%......I.BC
0020: 00 43 01 02 02 10 03 10  05 46 00 6E F0 FF FF 7F  .C.......F.n....
0030: 03 80 99 F0 FF FF 7F 02  04 10 04 80 00 46 00 29  .............F.)
0040: 0A 85 41 00 01 09 01 49  00 21 00                 ..A....I.!.     
```

#### Opcodes

```
  0: 0x0001 [0x4A] LocalPlayer looks at Clamming Point (ID: 16793993/0x01004189)
  1: 0x000A [0x48] [System] [7266*]:
    → "The area is littered with pieces of broken seashells."
  2: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000E [0x24] CREATE_DIALOG(message_id=7267*, default_option=0*, option_flags=0*)
    → "Dig here? [Yep./Nope.]"
  4: 0x0015 [0x25] WAIT_DIALOG_SELECT()
  5: 0x0016 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0049
  6: 0x001E [0x42] SET_CLI_EVENT_CANCEL_DATA()
  7: 0x001F [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  8: 0x0021 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  9: 0x0023 [0x02] IF !(Work_Zone[2] > Work_Zone[3]) GOTO 0x0046
 10: 0x002B [0x6E] LocalPlayer uses emote 39*
 11: 0x0032 [0x99] Wait for LocalPlayer animation to complete
 12: 0x0037 [0x02] IF !(Work_Zone[4] == 1*) GOTO 0x0046
 13: 0x003F [0x29] REQ_SET_WAIT(priority=0x0A, entity_id=Unnamed NPC (ID: 16793989/0x01004185), tag_num=0x09)
 14: 0x0046 [0x01] GOTO 0x0049

SUBROUTINE_0049:
 15: 0x0049 [0x21] END_EVENT
 16: 0x004A [0x00] END_REQSTACK()
```
