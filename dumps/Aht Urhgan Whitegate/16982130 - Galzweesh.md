# 16982130 - Galzweesh

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Aht Urhgan Whitegate (ID: 50) |
| Block Size       | 156 bytes                     |
| Total Events     | 2                             |
| References Count | 9                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [658](#event-658)     | 0x0001       |     94 |             24 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x0000      |           0 |
|       2 | 0x0001      |           1 |
|       3 | 0x18BA      |        6330 |
|       4 | 0x18BB      |        6331 |
|       5 | 0x18BC      |        6332 |
|       6 | 0x1A79      |        6777 |
|       7 | 0x1A7A      |        6778 |
|       8 | 0x1A7B      |        6779 |

## String References

- **6330**: Eh? You wanna know why these docks're called "Ephramad Port"? You really don't know?
- **6331**: Y'see, long ago, this city was the capital of a different nation. But Aht Urhgan, she kept expanding until she swallowed up all the countries around 'er.
- **6332**: The name Ephramad Port's a remnant from the time before this land belonged t' Aht Urhgan. Least, that's what my dad tells me.
- **6777**: Eh? You wanna know about the ghost ship!? You got a lotta guts t' bring that up in 'earing range of the palace...
- **6778**: The Immortals are branding anyone what talks about that spook ship as a member of the Seagull Phratrie. Be careful you don't get yourself 'auled away in chains.
- **6779**: But just between you an' me... I 'eard there's a bloke what saw a great shadow of a ship sailing through the mists of the Silver Sea. Says that 'e saw not one sailor on deck to guide 'er course...

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

### Event 658

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 94 bytes |
| Instructions | 24       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 66 01 80 F8 FF FF 7F   ........f......
0010: F8 FF FF 7F 74 6C 6B 30  13 00 00 02 80 02 00 00  ....tlk0........
0020: 01 80 80 34 00 1D 03 80  23 1D 04 80 23 1D 05 80  ...4....#...#...
0030: 23 01 4B 00 02 00 00 02  80 80 4B 00 1D 06 80 23  #.K.......K....#
0040: 1D 07 80 23 1D 08 80 23  01 4B 00 66 01 80 F8 FF  ...#...#.K.f....
0050: FF 7F F8 FF FF 7F 74 65  6E 30 1C 00 80 21 00     ......ten0...!. 
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(30* ticks)
  2: 0x0009 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=0*
  3: 0x0018 [0x13] ExtData[1]->WorkLocal[0] = rand() % 1*
  4: 0x001D [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x0034
  5: 0x0025 [0x1D] PRINT_EVENT_MESSAGE(message_id=6330*)
    → "Eh? You wanna know why these docks're called "Ephramad Port"? You really don't know?"
  6: 0x0028 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0029 [0x1D] PRINT_EVENT_MESSAGE(message_id=6331*)
    → "Y'see, long ago, this city was the capital of a different nation. But Aht Urhgan, she kept expanding until she swallowed up all the countries around 'er."
  8: 0x002C [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x002D [0x1D] PRINT_EVENT_MESSAGE(message_id=6332*)
    → "The name Ephramad Port's a remnant from the time before this land belonged t' Aht Urhgan. Least, that's what my dad tells me."
 10: 0x0030 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0031 [0x01] GOTO 0x004B
 12: 0x0034 [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x004B
 13: 0x003C [0x1D] PRINT_EVENT_MESSAGE(message_id=6777*)
    → "Eh? You wanna know about the ghost ship!? You got a lotta guts t' bring that up in 'earing range of the palace..."
 14: 0x003F [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0040 [0x1D] PRINT_EVENT_MESSAGE(message_id=6778*)
    → "The Immortals are branding anyone what talks about that spook ship as a member of the Seagull Phratrie. Be careful you don't get yourself 'auled away in chains."
 16: 0x0043 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x0044 [0x1D] PRINT_EVENT_MESSAGE(message_id=6779*)
    → "But just between you an' me... I 'eard there's a bloke what saw a great shadow of a ship sailing through the mists of the Silver Sea. Says that 'e saw not one sailor on deck to guide 'er course..."
 18: 0x0047 [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x0048 [0x01] GOTO 0x004B

SUBROUTINE_004B:
 20: 0x004B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ten0" with entities [EventEntity, EventEntity], work=0*
 21: 0x005A [0x1C] WAIT(30* ticks)
 22: 0x005D [0x21] END_EVENT
 23: 0x005E [0x00] END_REQSTACK()
```
